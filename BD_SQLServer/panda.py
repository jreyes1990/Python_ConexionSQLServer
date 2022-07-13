import pandas as pd
import pyodbc as db

cn = db.connect("Driver={ODBC Driver 17 for SQL Server}; "
                "server=JREYES1990; "
                "database=ReservaCine; "
                "Trusted_connection=yes")

df = pd.read_sql_query("select * from pais", cn)

ruta ="C:\Cursos\PYTHON\Proyecto\BD_ConexionConsultas\\dataframe.txt"
file = open(ruta,"w") #Genera archivo .txt
print(df)
file.write(str(df))