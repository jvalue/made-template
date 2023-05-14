import pandas as pd

df1 = pd.read_csv("zaehlstelle_weseler_2018_stundenauswertung.csv", sep=",")
df2 = pd.read_csv("Zaehlstelle_Weseler_Strasse_Stundenauswertung_2022.csv", sep=",")


### clean and extract the needed columns for dataset 1
df1 = df1.set_index("Zeit")
for el in df1.columns:
    if el != "Weseler Straße (gesamt)":
        df1 = df1.drop(columns=[el])
  
### clean and extract the needed columns for dataset 2
df2 = df2.set_index("Zeit")
for el in df2.columns:
    if el != "Weseler Straße":
        df2 = df2.drop(columns=[el])
              

df1.to_sql("fahraddverkehr_2018", "sqlite:///./data/fahraddverkehr_2018.sqlite", if_exists="replace", index=False)
df2.to_sql("fahraddverkehr_2022", "sqlite:///./data/fahraddverkehr_2022.sqlite", if_exists="replace", index=False)

