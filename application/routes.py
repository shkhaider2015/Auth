from flask import jsonify
from application import app


@app.route('/')
def home():
    return jsonify({ 'status' : 'ok' })


@app.route('/adduser', methods=['POST'])
def add_user():
    return jsonify({ 'status' : 'ok' })