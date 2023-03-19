import os
import sys

import flask
from flask import Flask, jsonify, request, Response

sys.path.insert(1, os.getcwd())

import server.parser as parser
from server.config import PORT, HOST

app = Flask(__name__)


@app.route('/parse', methods=['POST'])
def parsing_endpoint():
    try:
        # Get request data
        data = request.data

        # Process data and create response
        response_data = parser.parse_data(data)

        # Return response as JSON
        return jsonify({"uniquePids": response_data})
    except parser.ParsingException as e:
        response_data = jsonify({"error": str(e)})
        return flask.make_response(response_data, 400)
    except Exception as e:
        response_data = jsonify({"error": str(e)})
        return flask.make_response(response_data, 500)


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
