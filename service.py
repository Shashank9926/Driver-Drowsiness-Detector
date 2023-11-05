from flask import Flask
from flask import request
#from flask_cors import CORS,cross_origin


import dao

app = Flask(__name__)
#cors=CORS(app)
app.config['CORS_HEADER']='Content-Type'

@app.route('/session', methods=['GET', 'POST', 'PUT', 'DELETE'])
#@cross_origin()
def call_session():
    return dao.session_details()


@app.route('/sos', methods=['GET', 'POST', 'PUT', 'DELETE'])
#@cross_origin()
def call_sos():
    sosid = request.form.get("sosid")
    print(sosid)
    return dao.sos_details(sosid)



app.run(host="0.0.0.0", port=6068)
