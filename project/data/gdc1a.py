import sqlite3
import requests
import json
import pandas as pd

from data import Demographic, Diagnosis

def runGraphQLQuery(url, query, variables = {}, headers = {}):
    #accessToken = "xxx"
    #headers = {"Authorization": f"Bearer {accessToken}"}

    r = requests.post(url, json={"query": query, 'variables': variables}, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(), indent=2)
    else:
        raise Exception(f"Query failed to run with a {r.status_code}.")

def runGDCGraphQLQuery(first=None, after=None):
    url = "https://api.gdc.cancer.gov/v0/graphql"
    case_hit_first = "hits (filters: $filters_cases) "
    case_hit_next = """hits (filters: $filters_cases, first: {}, after: "{}") """.format(first, after)
    query1 = """
        query getgdcdata($filters_cases: FiltersArgument, $filters_diagnoses: FiltersArgument) {
        explore {
            cases {"""
    query2 = """{
            total
            pageInfo {
                endCursor
                hasNextPage
            }            
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
    query = query1+case_hit_first+query2
    if (after):
        query = query1+case_hit_next+query2
    variables = """{"filters_cases": {"op": "in", "content": {"field": "primary_site", "value": ["Kidney"]}}, "filsters_diagnoses": {}}"""
    return runGraphQLQuery(url, query, variables)

def prepareData(jsondata):
    jsonObject = json.loads(jsondata)

    demographics = []
    diagnoses = []
    pagination = [None]*3

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
            if "total" == attr:
                pagination[0] = obj
            if "hasNextPage" == attr:
                pagination[1] = obj
            if "endCursor" == attr:
                pagination[2] = obj

    recursive_iter(jsonObject)
    return demographics, diagnoses, pagination[0], pagination[1], pagination[2]

def loadToSink(path: str, demographics, diagnoses):
    con = sqlite3.connect('test_gdc.sqlite')

    df = pd.DataFrame([x.as_dict() for x in demographics])
    df.to_sql('demographic', con, if_exists='fail', index=False)
    df = pd.DataFrame([x.as_dict() for x in diagnoses])
    df.to_sql('diagnoses', con, if_exists='fail', index=False)
    
    con.commit()
    con.close()

response = runGDCGraphQLQuery(100) #run first 100 samples, get also pagination information, details see https://graphql.org/learn/pagination/
demographics, diagnoses, total, hasNextPage, endCursor = prepareData(response)
while hasNextPage:
    response = runGDCGraphQLQuery(500, endCursor)
    tmp_demographics, tmp_diagnoses, total, hasNextPage, endCursor = prepareData(response)
    demographics = demographics + tmp_demographics
    diagnoses = diagnoses + tmp_diagnoses
    print("Total: {}".format(total))
    print("Aktuell: {}".format(len(demographics)))
    print("Noch Daten vorhanden: {}".format(hasNextPage))

loadToSink("test_gdc.sqlite", demographics, diagnoses)