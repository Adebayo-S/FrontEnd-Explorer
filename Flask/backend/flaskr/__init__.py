from flask import Flask, jsonify, request, abort
from backend.models import setup_db, Plant
from flask_cors import CORS, cross_origin

PLANT_PER_PAGE = 8


def paginate_plants(request, plants):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * PLANT_PER_PAGE
    end = start + PLANT_PER_PAGE

    plants = [plant.format() for plant in plants]
    current_plants = plants[start:end]

    return current_plants


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)
    # CORS(app) -- most basic way of using CORS on your app
    # In the implementation below, resources takes in a dict of
    #       key (/api/*) : value (list of origins that will have access
    #       to that resource)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request  # adds some headers to the response
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response  # this method takes some response, edit and needs
        # to return the edited response to the client

    @app.route('/plants', methods=['GET', 'POST'])
    def get_plants():
        plants = Plant.query.all()
        current_plants = paginate_plants(request, plants)

        if len(current_plants) == 0:
            abort(404)

        return jsonify({
            "success": True,
            "plants": current_plants,
            "total_plants": len(plants)
        })

    @app.route('/plants/<int:plant_id>')
    def get_specific_plant(plant_id):
        plant = Plant.query.filter(Plant.id == plant_id).one_or_none()

        if plant is None:
            abort(404)

        return jsonify({
            'success': True,
            'plant': plant.format()
        })

    @app.route('/')
    def hello_world():
        return jsonify({'message': 'HELLO, WORLD!'})

    @app.route('/messages')
    @cross_origin()  # this decorator allows us to use the CORS decorator
    # just for this route/endpoint. It is used just before the method
    def get_messages():
        return 'GETTING MESSAGES'

    return app
