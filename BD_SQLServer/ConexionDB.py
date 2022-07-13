import pyodbc as db

cn = db.connect("Driver={ODBC Driver 17 for SQL Server}; "
                "server=JREYES1990; "
                "database=ReservaCine; "
                "Trusted_connection=yes")

cursor = cn.cursor()
cursor.execute("select * from dbo.pais;")

ruta ="C:\Cursos\PYTHON\Proyecto\BD_ConexionConsultas\\archivoPython.txt"
file = open(ruta,"w") #Genera archivo .txt

for fila in cursor: #write: sobreescribe en el archivo .txt
    for celda in fila:
        file.write(str(celda))
        file.write("-")
        print(celda)
    file.write("\n")
    print("_____________________________")
file.close()
