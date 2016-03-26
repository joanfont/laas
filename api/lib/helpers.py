import json
from flask import Response


def jsonify(data):
    json_data = json.dumps(data)
    return Response(json_data, content_type='application/json', mimetype='application/json')
