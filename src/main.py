"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import requests
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Person, Plant, Monitor
from flask_jwt_simple import (
    JWTManager, jwt_required, create_jwt, get_jwt_identity
)
from send_sms import send_msg
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)


app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_KEY')
jwt = JWTManager(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



@app.route('/register', methods=['POST'])
def handle_register():

    body = request.get_json()

    if 'fname' not in body:
        raise APIException('fname missing from body', 400)
    if 'lname' not in body:
        raise APIException('lname missing from body', 400)
    if 'email' not in body:
        raise APIException('email missing from body', 400)
    if 'phone' not in body:
        raise APIException('phone missing from body', 400)
    if 'password' not in body:
        raise APIException('password missing from body', 400)

    person = Person(
        fname = body['fname'],
        lname = body['lname'],
        email = body['email'],
        phone = body['phone'],
        password = body['password']
    )
    db.session.add(person)
    db.session.commit()

    person = Person.query.filter_by(email=body['email']).first()
    if not person:
        raise APIException('Person not found')

    return jsonify(person.serialize())



@app.route('/login', methods=['POST'])
def handle_login():

    body = request.get_json()

    if 'email' not in body:
        raise APIException('email missing from body', 400)
    if 'password' not in body:
        raise APIException('password missing from body', 400)

    user = Person.query.filter_by(email=body['email'], password=body['password']).first()

    if user is None:
        raise APIException('user not found', 404)

    return jsonify({
        'token': create_jwt(identity=body['email']),
        'user': user.serialize()
    }), 200




@app.route('/get_plant', methods=['POST'])
def handle_hello():

    body = request.get_json()

    url = 'https://trefle.io/api/plants?token=NUl6YXBQa3RiVmlJQVVMZWZ2cWYxUT09&q=' + body["name"]
    header = {"Authorization": "Bearer NUl6YXBQa3RiVmlJQVVMZWZ2cWYxUT09"}

    response = requests.get(url, headers=header)
    data = response.json()

    return jsonify({'data': data})



@app.route('/test')
def test():

    person = Person.query.filter_by(email='ooohhh').first()
    if not person:
        raise APIException('Person not found')
    return jsonify(person.serialize())
    return jsonify({'msg':'exactly'})




# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
