import sqlite3
import pandas as pd
import os

# current_dir = os.path()

df1_xslx = pd.read_excel("https://www.stadt-muenster.de/fileadmin/user_upload/stadt-muenster/61_verkehrsplanung/pdf/zaehlstelle_weseler_2018_stundenauswertung.xlsx", engine="openpyxl")
df2_xslx = pd.read_excel("https://www.stadt-muenster.de/fileadmin/user_upload/stadt-muenster/61_verkehrsplanung/pics/radverkehr/Zaehldaten_2022/Zaehlstelle_Weseler_Strasse_Stundenauswertung_2022.xlsx", engine="openpyxl")
# df1 = pd.read_csv("zaehlstelle_weseler_2018_stundenauswertung.csv", sep=",")
# df2 = pd.read_csv("Zaehlstelle_Weseler_Strasse_Stundenauswertung_2022.csv", sep=",")

# df2_xslx.set_index("Zeitraum")

# ### clean and extract the needed columns for dataset 1
# df1 = df1.set_index("Zeit")
# for el in df1.columns:
#     if el != "Weseler Straße (gesamt)":
#         df1 = df1.drop(columns=[el])
  
# ### clean and extract the needed columns for dataset 2
# df2 = df2.set_index("Zeit")
# for el in df2.columns:
#     if el != "Weseler Straße":
#         df2 = df2.drop(columns=[el])
              
              
conn = sqlite3.connect("data/verkehrszaehlung.sqlite")

df1_xslx.to_sql("fahraddverkehr_2018", conn, if_exists="replace")
df2_xslx.to_sql("fahraddverkehr_2022", conn, if_exists="replace")

