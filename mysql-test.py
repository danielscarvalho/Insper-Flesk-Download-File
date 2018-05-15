
# pip install mysql-connector

from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='scott', 
                                 password='tiger',
                                 host='127.0.0.1',
                                 database='bigdata')
cursor = cnx.cursor()

query = "SELECT NOW() AGORA, 145/2 VALOR, VERSION() VERSAO"

cursor.execute(query)

for (agora, valor, versao) in cursor:
    print("{} -> {} -> {}".format(agora, valor, versao))

cnx.close()