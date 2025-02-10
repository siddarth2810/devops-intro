import os
from flask import Flask, request  
from dotenv import load_dotenv 
import logging

load_dotenv()
app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)  

@app.before_request
def log_request():
    logging.info(f"Request: {request.method} {request.path}") 


@app.route('/')
def home():
    return "hello devops"

@app.route('/health') 
def health():
    return {"status": "up"}, 200

if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(port=port, debug=True) 
