from application import app
from flask import jsonify


@app.route('/')
def home():
    return jsonify({ 'status' : 'ok' })