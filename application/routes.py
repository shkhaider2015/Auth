from flask import jsonify, request
from application import app


@app.route('/')
def home():
    return jsonify({ 'status' : 'ok' })


@app.route('/adduser', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    image_file = request.files['image_file']
    return jsonify({ 'status' : 'ok', 'name' : name })