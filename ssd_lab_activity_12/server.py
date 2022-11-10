from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)
login_manager = LoginManager()

login_manager.init_app(app)

class User(UserMixin, db.Model):
    username = db.Column(db.String(25), primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(80), nullable=True)


@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

def test_connection():
    with app.app_context():
        db.create_all()
        app.run(debug=True)
        
@app.route("/user/signup", methods=["POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        register = User(username = username, email = email, password = password)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html") 
        

@app.route('/user/signin', methods=['POST'])
def do_signin():
    if(request.method == 'POST'):
        req = request.get_json()
        
        email = req['email']
        password = req['password']
        check_user = User.query.filter_by(email=email).first()
        
        if(check_user is not None):
            if(check_user.password == password):
                login_user(check_user)
                return jsonify(**{'result': 200, 'data': {'message': 'login success'}})
            else:
                return jsonify(**{'result': 500, 'data': {'message': 'Incorrect Password'}})
        else:
            return jsonify(**{'result': 500, 'data': {'message': 'No such user'}})
        

@app.route('/user/signout')
def logout():
    session.clear()
    return jsonify(**{'result': 200, 'data': {'message': 'logout success'}})


test_connection()
