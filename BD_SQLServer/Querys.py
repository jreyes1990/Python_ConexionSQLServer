import pandas as pd
import pyodbc as db
import configparser

class SQL:
    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read("ConexionConfig.cs")
        driver = conf.get("Cadena", "Driver")
        server = conf.get("Cadena", "Server")
        database = conf.get("Cadena", "Database")
        trusted = conf.get("Cadena", "Trusted_Conecc")
        self.Cadena = "Driver={0}; " \
                      "server={1}; " \
                      "database={2}; " \
                      "Trusted_connection={3}" \
                      "".format(driver, server, database, trusted)

    def listar(self, consulta):
        cn = db.connect(self.Cadena)
        df = pd.read_sql_query(consulta, cn)
        data = df.to_html(index=False)
        return data