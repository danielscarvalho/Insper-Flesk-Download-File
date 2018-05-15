from flask import Flask, stream_with_context
from werkzeug.datastructures import Headers
from werkzeug.wrappers import Response
from mysql.connector import (connection)

app = Flask(__name__)

def getDataBaseFile(id):   
    
    cnx = connection.MySQLConnection(user='scott', 
                                     password='tiger',
                                     host='127.0.0.1',
                                     database='bigdata')
    cursor = cnx.cursor()
 
    #BIG_FILE -> BLOB
    query = "SELECT FILE_NAME, BIG_FILE FROM BIGDATA.FILE_STORE " \
        + "WHERE ID=\"%s\";"

    cursor.execute(query, id)
    
    row = cursor.fetchone()
    
    print(row)
    
    file_name = row['FILE_NAME'] #FILE_NAME
    file_data = row['BIG_FILE'] #BIG_FILE - DADOS...

    return [file_name, file_data]

@app.route('/file/<id>')
def download_file(id):
  
    file_name, file_content = getDataBaseFile(id)
  
    # add a filename - HTTP
    headers = Headers()
    headers.set('Content-Disposition', 'attachment', filename=file_name)

    # stream the response as the data is generated
    return Response(
        stream_with_context(file_content),
        mimetype='application/pdf', headers=headers #https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Basico_sobre_HTTP/MIME_types/Complete_list_of_MIME_types
    )

app.run()