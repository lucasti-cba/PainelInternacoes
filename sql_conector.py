import cx_Oracle  
from datetime import datetime , date
import sys
import os
import time




import cx_Oracle

uid = "tasy"    # usuário
pwd = "aloisk"   # senha
db = "TASY"  # string de conexão do Oracle, configurado no
                # cliente Oracle, arquivo tnsnames.ora
 
conn = cx_Oracle.connect(uid+"/"+pwd+"@"+db) 

c = conn.cursor()


def getdados():
	dados = []
	date1 = date.today()
	print(date1)
	c.execute("SELECT *  FROM TASY.PACIENTE_INTERNADO_V2  WHERE TASY.PACIENTE_INTERNADO_V2.DT_SAIDA_UNIDADE IS NULL ")
	dados = c.fetchall()
	for row in dados:
		print(row)
	return dados


getdados()


