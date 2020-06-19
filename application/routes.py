from flask import jsonify, request
from application import app


@app.route('/')
def home():
    return jsonify({ 'status' : 'ok' })


@app.route('/adduser', methods=['POST'])
def add_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    # image_file = request.files['image_file']
    print(f" Name : {name} \n Email : {email} \n Password : {password} ")

    return jsonify({ 'name' : name, 'emai' : email, 'password' : password })