from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # CORS(app) -- most basic way of using CORS on your app
    # In the implementation below, resources takes in a dict of
    #       key (/api/*) : value (list of origins that will have access
    #       to that resource)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request  # adds some headers to the response
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response  # this method takes some response, edit and needs
        # to return the edited response to the client

    @app.route('/')
    def hello_world():
        return jsonify({'message': 'HELLO, WORLD!'})

    @app.route('/messages')
    @cross_origin()  # this decorator allows us to use the CORS decorator
    # just for this route/endpoint. It is used just before the method
    def get_messages():
        return 'GETTING MESSAGES'

    return app
