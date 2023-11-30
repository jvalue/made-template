from sqlalchemy import create_engine, inspect

from pipeline import (
    data_extraction_xls,
    data_transformation
)


def test_dataset_extraction(path):
    df = data_extraction_xls(path)
    assert not df.empty, "Dataset Extraction Failed"
    print("Extract Dataset: Test Passed")
    return df


def test_dataset_transformation(data, rename_col, drop_col):
    df = data_transformation(data, rename_col, drop_col)
    assert df.isna().any().any() == False, "Invalid data Found in Dataset"
    print("Dataset Transformation: Test Passed")
    return df


def test_dataset_loader(table_name):
    engine = create_engine(f"sqlite:///datasets.sqlite")

    # Create an inspector object
    inspector = inspect(engine)

    # Check if a table exists in the database
    exists = inspector.has_table(table_name)
    assert exists, f"The table '{table_name}' does not exist in the database."
    print("test_dataset_loader: " + table_name + "Table exists, Test Passed")


def test_pipeline():
    path_Immoscout24 = "https://docs.google.com/spreadsheets/d/1Bhi9CZjfI6qlM-2J1TVeDy_JfIcSBqufXlHV6IuT7n4/export?format=xlsx"
    df1 = test_dataset_extraction(path_Immoscout24)
    df1_drop_cols = ["picturecount", "scoutId", "geo_bln", "geo_krs"]
    df1_rename_cols = {
        "regio1": "federalState",
        "geo_plz": "zipCode",
        "regio2": "district",
        "regio3": "cityTown"
    }

    test_dataset_transformation(df1, df1_rename_cols, df1_drop_cols)

    test_dataset_loader("immoscout")

    path_intstudent = "https://docs.google.com/spreadsheets/d/1n9DXXIBUI5VpP8-qgCdhxvoV6FJgUyAVrz1VxAFZVNo/export?format=xlsx"
    df2 = test_dataset_extraction(path_intstudent)
    df2_drop_cols = []
    df2_rename_cols = {
        "stadt": "city",
        "universität": "university",
        "Geisteswissenschaften": "Humanities",
        "Sozialwissenschaften": "Social sciences",
        "Mathematik": "Mathematics",
        "Ingenieurwissenschaften": "Engineering sciences",
        "Informatik": "Computer Science",
        "Medizin": "Medicine",
        "Landwirtschaft": "Agriculture"
    }

    test_dataset_transformation(df2, df2_rename_cols, df2_drop_cols)

    test_dataset_loader("intstudents")


if __name__ == "__main__":
    test_pipeline()