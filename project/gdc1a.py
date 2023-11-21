import sqlite3
import requests
import json
import pandas as pd
import sqlalchemy

from data.data import Demographic, Diagnosis

def runGraphQLQuery(url, query, variables = {}, headers = {}):
    #accessToken = "xxx"
    #headers = {"Authorization": f"Bearer {accessToken}"}

    r = requests.post(url, json={"query": query, 'variables': variables}, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(), indent=2)
    else:
        raise Exception(f"Query failed to run with a {r.status_code}.")


def runRESTQuery(url, fields: list):
    fields = ','.join(fields)
    params = {
        "fields": fields,
        "format": "TSV",
        "size": "100"
    }
    response = requests.get(url, params = params)
    return response

def runCasesRestQuery():
    cases_endpt = "https://api.gdc.cancer.gov/cases"
    fields = [
        "submitter_id",
        "case_id",
        "primary_site",
        "disease_type",
        "diagnoses.vital_status"
    ]
    return runRESTQuery(cases_endpt, fields)

def runProjectsGraphQLQuery():
    url = "https://api.gdc.cancer.gov/v0/graphql"
    query = """
        query getgdcdata($filters_cases: FiltersArgument, $filters_diagnoses: FiltersArgument) {
        explore {
            cases {
            hits (filters: $filters_cases) {
                edges {
                node {
                    id,
                    index_date,
                    primary_site,
                    disease_type,
                    diagnoses {
                    hits (filters: $filters_diagnoses) {
                        edges {
                        node {
                            ajcc_clinical_t,
                            ajcc_clinical_n,
                            ajcc_clinical_m,
                            ajcc_clinical_stage,
                            ajcc_pathologic_t,
                            ajcc_pathologic_n,
                            ajcc_pathologic_m,
                            ajcc_pathologic_stage
                        }
                        }
                    }
                    },
                    demographic {
                    age_at_index,
                    days_to_birth,
                    days_to_death,
                    cause_of_death,
                    cause_of_death_source,
                    country_of_residence_at_enrollment,
                    state,
                    vital_status
                    }
                }
                }
            } 
            }
        }
        }
    """
    variables = """{ "filters_cases": {}, "filsters_diagnoses": {}}"""
    #TODO use pagination to get more results https://graphql.org/learn/pagination/
    return runGraphQLQuery(url, query, variables)

def loadToSink(path: str, jsondata):
    jsonObject = json.loads(jsondata)

    demographics = []
    diagnoses = []

    def recursive_iter(obj, keys=()):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if "demographic" == k:
                    demographics.append(Demographic())
                if "diagnoses" == k:
                    diagnoses.append(Diagnosis())
                recursive_iter(v, keys + (k,))
        elif any(isinstance(obj, t) for t in (list, tuple)):
            for idx, item in enumerate(obj):
                recursive_iter(item, keys + (idx,))
        else:
            attr = keys[len(keys)-1]
            if "demographic" in keys:
                objDemo = demographics[len(demographics)-1]
                if "age_at_index" == attr:
                    objDemo.age_at_index = obj
            if "diagnoses" in keys:
                objDiag = diagnoses[len(diagnoses)-1]
                if "ajcc_pathologic_t" == attr:
                    objDiag.ajcc_pathologic_t = obj
                if "ajcc_pathologic_n" == attr:
                    objDiag.ajcc_pathologic_n = obj
                if "ajcc_pathologic_m" == attr:
                    objDiag.ajcc_pathologic_m = obj
            if "id" == attr:
                demographics[len(demographics)-1].case_id = obj
                diagnoses[len(diagnoses)-1].case_id = obj

    #nodes = jsonObject["data"]["explore"]["cases"]["hits"]["edges"]
    recursive_iter(jsonObject)

    con = sqlite3.connect('test_gdc.sqlite')

    df = pd.DataFrame([x.as_dict() for x in demographics])
    print(df)
    df.to_sql('demographic', con, if_exists='fail', index=False)
    df = pd.DataFrame([x.as_dict() for x in diagnoses])
    print(df)
    df.to_sql('diagnoses', con, if_exists='fail', index=False)
    
    con.commit()
    con.close()

response = runProjectsGraphQLQuery()
print(response)
loadToSink("test_gdc.sqlite", response)