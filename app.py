from flask import Flask, jsonify, request
from database import db
from models.User import User
from flask_login import  LoginManager, login_user

app = Flask(__name__)
login_manager = LoginManager()

app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
login_manager.login_view = "login"

db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login",methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
       user = User.query.filter_by(username=username).first()

       if user and user.password == password:
            login_user(user)
            return jsonify({"message":"Login Realizado com sucesso"}),400


    return jsonify({"message":"Credenciais Inválidas"}),400



if __name__ == "__main__":
    app.run(debug=True)