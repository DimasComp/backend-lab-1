from flask import Blueprint, jsonify
from datetime import datetime
import pytz

main = Blueprint('main', __name__)


@main.route('/healthcheck')
def healthcheck():
    timezone = pytz.timezone('Etc/GMT-2')
    current_time = datetime.now(timezone)
    return jsonify({'status': 'ok', 'datetime': current_time.strftime('%d-%m-%Y %H:%M:%S')})