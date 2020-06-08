from flask import jsonify, request
from application import app


@app.route('/')
def home():
    return jsonify({ 'status' : 'ok' })


@app.route('/adduser', methods=['POST'])
def add_user():
    naem = request.json['name']
    email = request.json['email']
    image_file = request.json['password']
    return jsonify({ 'status' : 'ok', 'name' : naem })