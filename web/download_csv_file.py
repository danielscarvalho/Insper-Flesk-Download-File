from flask import Flask, stream_with_context
from werkzeug.datastructures import Headers
from werkzeug.wrappers import Response

app = Flask(__name__)

def getCsvFile(id):
    return "{0};A;100;2,3\n{0};B;300;3,1\n{0};A;234;0,4".format(id)

@app.route('/file/<id>')
def download_file(id):
  
    # add a filename
    headers = Headers()
    headers.set('Content-Disposition', 'attachment', filename='data.csv')

    # stream the response as the data is generated
    return Response(
        stream_with_context(getCsvFile(id)),
        mimetype='text/csv', headers=headers
    )

app.run()