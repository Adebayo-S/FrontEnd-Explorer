from flask import Flask, jsonify
import os


def create_app(test_config=None):
    # __name__ tells the app which dir it's housed in
    # so if there's any additional config or relative path it's
    # looking for, it knows where to go

    # the second argument passed simply says if there's going to be
    # any config in the same project dir, look relative to the instance
    app = Flask(__name__  # , instance_relative_config=True #
                )
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Note: Don't have multiple app route decorators for the
    # same route. Unique routes and methods.

    # to send anything more complex than as string,
    # jsonify is used to format our response

    @app.route('/')
    def hello():
        return jsonify({'message': 'Hello, World!'})

    @app.route('/smiley')
    def smiley():
        return ':)'

    return app


