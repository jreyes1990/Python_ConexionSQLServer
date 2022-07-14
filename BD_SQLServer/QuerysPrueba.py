import Querys

odasql = Querys.SQL()
rpta = odasql.listar("select * from pais")
print(rpta)