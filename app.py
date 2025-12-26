from flask import Flask, jsonify, request
from database import db
from models.User import User
from flask_login import  LoginManager, login_required, login_user, logout_user, current_user

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

@app.route("/logout",methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({
        "message": "Logout realizado com sucesso"
    })

@app.route("/register",methods=["POST"])
def register():
    data = request.json
    username = data["username"]
    password= data["password"]

    if data and username and password:
        user = User.query.filter_by(username=username).first()

        if user:
            return jsonify({"message":"Já existe um usuário com esse username"}),400

        newUser = User(username=username,password=password)
        db.session.add(newUser)
        db.session.commit()

        return jsonify({"message":f"Usuário {newUser.username} criado com sucesso"})

    return jsonify({
        "message":"O username e senha são obrigatórios"
    }),400


@app.route("/users/<int:user_id>",methods=["GET"])
@login_required
def get_profile(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message":"Usuário não encontrado"}),404
    
    return jsonify({"user":{
        "username":user.username
    }})

@app.route("/users/<int:user_id>",methods=["PUT"])
@login_required
def update_user(user_id):
    data = request.json
  
    if not data.get("password"):
     return  jsonify({"message":"Senha é obrigatória"}),400

    user = User.query.get(user_id)
    
    if not user:
     return jsonify({"message":"Usuário não encontrado"}),404

    user.password = data.get("password")

    db.session.commit()

    return jsonify({"message":f"A senha do usuário {user.username} foi editado com sucesso"})

@app.route("/users/<int:user_id>",methods=["DELETE"])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    
    if current_user.id == user.id:
        return jsonify({"message":"Não permitido"}),401

    if not user:
     return jsonify({"message":"Usuário não encontrado"}),404

    db.session.delete(user)

    db.session.commit()

    return jsonify({"message":f"O usuário foi excluido com sucesso"})
    
    

if __name__ == "__main__":
    app.run(debug=True)

