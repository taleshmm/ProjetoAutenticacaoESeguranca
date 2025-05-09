from flask import Blueprint, jsonify

bank_routes_bp = Blueprint('banck_routes', __name__)

@bank_routes_bp.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from the bank routes!"}), 200