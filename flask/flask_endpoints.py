from flask import Flask, request, make_response, send_file

app = Flask(__name__)

@app.route('/resume', methods=['GET'])
def get_resume():
    file_name = 'Resume.pdf'
    return send_file(file_name, as_attachment=False, mimetype='application/pdf')

@app.route('/flask')
def flask_home():
    return "Flask is running on borikanes.me"

if __name__ == '__main__':
    app.run('0.0.0.0',port=5001,debug=True)
