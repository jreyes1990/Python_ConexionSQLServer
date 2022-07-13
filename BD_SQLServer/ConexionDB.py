import pyodbc as db

cn = db.connect("Driver={ODBC Driver 17 for SQL Server}; "
                "server=JREYES1990; "
                "database=ReservaCine; "
                "Trusted_connection=yes")

cursor = cn.cursor()
cursor.execute("select * from dbo.pais;")
for fila in cursor:
    for celda in fila:
        print(celda)
    print("_____________________________")
