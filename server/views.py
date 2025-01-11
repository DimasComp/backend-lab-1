from flask import Blueprint, jsonify

main = Blueprint('main', __name__)


@main.route('/healthcheck')
def healthcheck():
    return jsonify({'status': 'ok'})