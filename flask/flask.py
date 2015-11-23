from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/resume')
def get_resume:
    with open('/Resume.pdf', 'rb') as pdf:
        return send_file(pdf, attachment_filename='Resume.pdf')
