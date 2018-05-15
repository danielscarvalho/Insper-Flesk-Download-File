
# pip install mysql-connector
# Reference: http://www.mysqltutorial.org/python-mysql-blob/

from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='scott', 
                                 password='tiger',
                                 host='127.0.0.1',
                                 database='bigdata')
cursor = cnx.cursor()

arquivo = open('data/dog4.jpg','rb')
dog_bdata = arquivo.read()
arquivo.close()

arquivo = open('data/dados.xlsx','rb')
planilha_bdata = arquivo.read()
arquivo.close()

arquivo = open('data/grocerylists.pdf','rb')
gl_bdata = arquivo.read()
arquivo.close()

################
args = ("dog3.jpg" ,"Maria Silva", dog_bdata)

query = "INSERT INTO BIGDATA.FILE_STORE(FILE_NAME, USER_OWNER, BIG_FILE)" \
        + "VALUE(%s ,%s, %s);"

cursor.execute(query, args)

####################
args = ("dados.xlsx" ,"Maria Silva", planilha_bdata)

query = "INSERT INTO BIGDATA.FILE_STORE(FILE_NAME, USER_OWNER, BIG_FILE)" \
        + "VALUE(%s ,%s, %s);"

cursor.execute(query, args)

###############
args = ("grocerylists.pdf" ,"Maria Silva", gl_bdata)

query = "INSERT INTO BIGDATA.FILE_STORE(FILE_NAME, USER_OWNER, BIG_FILE)" \
        + "VALUE(%s ,%s, %s);"

cursor.execute(query, args)



cnx.commit()

cnx.close()