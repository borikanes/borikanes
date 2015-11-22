from flask import Flask, request

app = Flask(__name__)

@app.route('/resume')
def get_resume:
    
