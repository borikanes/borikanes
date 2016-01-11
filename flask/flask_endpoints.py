from flask import Flask, request, make_response, send_file
from twilio.rest import TwilioRestClient
import os

app = Flask(__name__)
account_sid = os.environ.get('TWILIO_SID_KEY')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

@app.route('/resume', methods=['GET'])
def get_resume():
    file_name = 'Resume.pdf'
    return send_file(file_name, as_attachment=False, mimetype='application/pdf')

@app.route('/flask')
def flask_home():
    return "Flask is running on borikanes.me"

@app.route('/twilio', methods=['POST'])
def post_twilio():
    

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
