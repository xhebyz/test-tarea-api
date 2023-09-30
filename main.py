import os

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required
from flask_magql import MagqlExtension
import graphql_schema
from data.objects import Tarea
from database.mongo import MongoDB
from exceptions.handler import ExceptionHandler
from logic.tarea import TareaLogic
from auth.jwt import create_token

app = Flask(__name__)
load_dotenv()
app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET")  # Cambia esto a una clave secreta segura en producción
jwt = JWTManager(app)
magql_ext = MagqlExtension(graphql_schema.schema)
magql_ext.init_app(app)

db = MongoDB()
tarea_logic = TareaLogic(db)
collection_tarea = db.get_collection("tarea")


@app.route('/hi', methods=['POST', 'GET'])
def hi():
    return jsonify({"message": "world"}), 200


@app.route('/tareas', methods=['POST'])
@jwt_required()
def new_tarea():
    data = request.json
    tarea = Tarea.from_dict(data)
    tarea_id = tarea_logic.add_tarea(tarea.to_dict())
    return jsonify({'message': 'Tarea creada', 'id': str(tarea_id)}), 201


@app.route('/tareas', methods=['GET'])
@jwt_required()
def get_all_tareas():
    list_tarea = tarea_logic.get_all_tareas()
    return jsonify(list_tarea), 200


@app.route('/tareas/<int:tarea_id>', methods=['GET'])
@jwt_required()
def get_tarea(tarea_id):
    tarea = tarea_logic.get_tarea_id(tarea_id)
    return jsonify(tarea), 200


@app.route('/tareas/<int:tarea_id>', methods=['PUT'])
@jwt_required()
def update_tarea(tarea_id):
    data = request.json
    tarea = Tarea.from_dict(data)
    tarea_logic.update_tarea(tarea_id, tarea.to_dict())
    return jsonify({'message': 'Tarea actualizada correctamente'}), 200


@app.route('/tareas/<int:tarea_id>', methods=['DELETE'])
@jwt_required()
def delete_tarea(tarea_id):
    tarea_logic.eliminar_tarea(tarea_id)
    return jsonify({'message': 'Tarea eliminada correctamente'}), 200


@app.route('/jwt', methods=['POST'])
def get_token():
    data = request.json
    access_token = create_token(data.get("user_id"), data.get("password"))
    return jsonify(access_token=access_token), 200

@app.errorhandler(Exception)
def handle_exception(error):
    return ExceptionHandler.handle_exception(error)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
