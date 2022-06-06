from flask import jsonify, request
from user import app, Bcrypt, routes
from .models import user
import jwt

@app.route("/")
def home():
    return "This page is connected"


@app.route ("/register", methods=['GET', 'POST'])
def register():
    json_data = request.join
    if request.method == 'POST':
        hash_password = Bcrypt.generate_password_hash(json_data['password'])
        print("hello from try")
        try:
        
            users = user(
                    fullname = json_data['fullname'],
                    email = json_data['email'],
                    password = hash_password,
                    phone = json_data['phone']
                    )
            users.save()
            userdata = user.to_json()
            return jsonify(userdata)

        except Exception as err:
            print(err)
            return jsonify({"error": "internal server error"})

@app.route("/login", method = ["POST"])
def login():
    json_data = request.join
    if request.method == 'POST':
        try:
            usr = user.objects.get(email = json_data['email'])
            passwordcompare = Bcrypt.check_password_hash(usr.password, json_data['password'])
            userdata = usr.to_json()
            print(passwordcompare)
            encoded = jwt.encode({"id": userdata['id']})
            if (passwordcompare):
                return jsonify(token = str(encoded))
            else:
                return jsonify({"error": "invalid password"})
        except Exception as err:
            print(err)
            return jsonify ({"error":"internal server error"})

@app.route("/profile", methods = ['GET'])
def profile ():
    if request.method == "GET":
        try:
            if(request.headers["auth-token"]):
                token = request.headers["auth-token"]
                print(token)
                data = jwt.decode(token, "secretkey", algorithms = "HS256")
                user = user.objects.get(pk=data["id"])
                userdata = user.to_json()
                del userdata["password"]
                return jsonify(userdata)
            else:
                return jsonify(error="provide auth-token")
        except:
            return jsonify(error = "internal server error")