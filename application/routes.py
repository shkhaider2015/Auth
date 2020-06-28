from flask import jsonify, request
from application import app, db
from application.models import User


@app.route('/')
def home():
    return jsonify({ 'status' : 'ok' })


@app.route('/createuser', methods=['POST'])
def add_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    # image_file = request.files['image_file']
    print(f" Name : {name} \n Email : {email} \n Password : {password} ")
    user = User(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({ 'name' : name, 'emai' : email, 'password' : password })

@app.route('/checkemail/<string:email>', methods=['GET'])
def checkAvailablity(email):
    email = email
    user = User.query.filter_by(email=email).first()
    if user:
        print(user.name)
        return jsonify({ 'name' : user.name, 'email' : user.email, 'password' : user.password})
    else:
        print("User Is None")
        return jsonify({ 'name' : None, 'email' : None, 'password' : None })