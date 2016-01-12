from flask import Flask, request, make_response, send_file, jsonify, Response
from twilio.rest import TwilioRestClient
import os

app = Flask(__name__)
account_sid = os.environ.get('TWILIO_SID_KEY')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = TwilioRestClient(account_sid, auth_token)

@app.route('/resume', methods=['GET'])
def get_resume():
    file_name = 'Resume.pdf'
    return send_file(file_name, as_attachment=False, mimetype='application/pdf')

@app.route('/flask')
def flask_home():
    return "Flask is running on borikanes.me"

@app.route('/twilio', methods=['POST'])
def post_twilio():
    client.messages.create(
	   to=request.data,
	   from_="+13016837812",
	   body="Successfully sent a text message to the customer",
    )
    return error200("Successful")

@app.errorhandler(200)
def error200(e):
    response = jsonify(data=[])
    return response, 200

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
