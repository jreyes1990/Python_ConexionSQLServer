import pandas as pd
import pyodbc as db
import configparser
import openpyxl

config = configparser.ConfigParser()
config.read("ConexionConfig.cs")
driver = config.get("Cadena","Driver")
server = config.get("Cadena","Server")
database = config.get("Cadena","Database")
trusted = config.get("Cadena","Trusted_Conecc")

cn = db.connect("Driver={0}; "
                "server={1}; "
                "database={2}; "
                "Trusted_connection={3}".format(driver,server,database,trusted))

df = pd.read_sql_query("select * from cine", cn)

ruta ="C:\Cursos\PYTHON\Proyecto\BD_ConexionConsultas\\dataframe.txt"
rutaExcel ="C:\Cursos\PYTHON\Proyecto\BD_ConexionConsultas\\dataframe.xlsx"
rutaHTML ="C:\Cursos\PYTHON\Proyecto\BD_ConexionConsultas\\dataframe.html"
rutaJSON ="C:\Cursos\PYTHON\Proyecto\BD_ConexionConsultas\\dataframe.json"

#file = open(ruta,"w") #Genera archivo .txt
#fileExcel = open(rutaExcel,"w") #Genera archivo .txt

print(df)
#file.write(str(df))
#file.close()
df.to_csv(ruta,index=False)
df.to_excel(rutaExcel,index=False)
df.to_html(rutaHTML,index=False)
df.to_json(rutaJSON,orient="records")