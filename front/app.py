import requests
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

FASTAPI_URL = os.getenv('API_URL')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_one', methods=['POST'])
def clasificar_uno():
    file = request.files['file']
    response = requests.post(
        f"{FASTAPI_URL}/predict_one",
        files={'file': (file.filename, file.stream, file.mimetype)}
    )
    return response.text  

@app.route('/predict_various', methods=['POST'])
def clasificar_multiples():
    files = request.files.getlist('files')
    file_data = [('files', (f.filename, f.stream, f.mimetype)) for f in files]
    response = requests.post(
        f"{FASTAPI_URL}/clasificar-multiples",
        files=file_data
    )
    return response.text

@app.route('/reentrain', methods=['POST'])
def reentrenar():
    files = request.files.getlist('training_files')
    file_data = [('training_files', (f.filename, f.stream, f.mimetype)) for f in files]
    response = requests.post(
        f"{FASTAPI_URL}/reentrenar",
        files=file_data
    )
    return response.text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
