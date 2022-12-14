import time
from flask import jsonify


def default_response(data, status=200, start_time=None):
    response = jsonify(data=data, status=status, time_spend=(time.time() - start_time))

    return response
