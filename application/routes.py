from flask import jsonify, request, abort
from application import app, db, login_manager
from application.models import User
from flask_login import login_required, login_user


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

@app.route("/login/<string:email>+<string:password>", methods=['GET'])
def login_route(email, password):
    em = email
    pas = password
    print(em, pas)
    user = User.query.filter_by(email=email).first()
    if user:
        if user.password == password:
            login_user(user, remember=True)
            return jsonify({ 'email' : user.email, 'password' : user.password })
            
        else:
            return abort(404)
    else:
        return abort(404)


@app.route("/index")
@login_required
def index_home():
    return jsonify({ 'status' : "user is logged in" })
