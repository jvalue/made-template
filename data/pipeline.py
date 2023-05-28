import sqlite3
import pandas as pd
import os


df1_xslx = pd.read_excel("https://www.stadt-muenster.de/fileadmin/user_upload/stadt-muenster/61_verkehrsplanung/pdf/zaehlstelle_weseler_2018_stundenauswertung.xlsx", engine="openpyxl")
df2_xslx = pd.read_excel("https://www.stadt-muenster.de/fileadmin/user_upload/stadt-muenster/61_verkehrsplanung/pics/radverkehr/Zaehldaten_2022/Zaehlstelle_Weseler_Strasse_Stundenauswertung_2022.xlsx", engine="openpyxl")
            
              
conn = sqlite3.connect("verkehrszaehlungen.sqlite")

df1_xslx.to_sql("fahraddverkehr_2018", conn, if_exists="replace")
df2_xslx.to_sql("fahraddverkehr_2022", conn, if_exists="replace")
