from flask import Flask, request, jsonify

import graphql_schema
from database.mongo import MongoDB
from data.objects import Tarea
from logic.tarea import TareaLogic
import os
from dotenv import load_dotenv
from exceptions.handler import ExceptionHandler
from flask_magql import MagqlExtension
import magql

app = Flask(__name__)
magql_ext = MagqlExtension(graphql_schema.schema)
magql_ext.init_app(app)
load_dotenv()

db = MongoDB()
tarea_logic = TareaLogic(db)

collection_tarea = db.get_collection("tarea")

@app.route('/hi', methods=['POST', 'GET'])
def hi():
    return jsonify({"message" : "world"}), 200

@app.route('/tareas', methods=['POST'])
def new_tarea():
    data = request.json
    tarea = Tarea.from_dict(data)
    tarea_id = tarea_logic.add_tarea(tarea.to_dict())
    return jsonify({'message': 'Tarea creada', 'id': str(tarea_id)}), 201


@app.route('/tareas', methods=['GET'])
def get_all_tareas():
    list_tarea = tarea_logic.get_all_tareas()
    return jsonify(list_tarea), 200


@app.route('/tareas/<string:tarea_id>', methods=['GET'])
def get_tarea(tarea_id):
    tarea = tarea_logic.get_tarea_id(tarea_id)
    return jsonify(tarea), 200


@app.route('/tareas/<string:tarea_id>', methods=['PUT'])
def update_tarea(tarea_id):
    data = request.json
    tarea = Tarea.from_dict(data)
    tarea_logic.update_tarea(tarea_id, tarea.to_dict())
    return jsonify({'message': 'Tarea actualizada correctamente'}), 200


@app.route('/tareas/<string:tarea_id>', methods=['DELETE'])
def delete_tarea(tarea_id):
    tarea_logic.eliminar_tarea(tarea_id)
    return jsonify({'message': 'Tarea eliminada correctamente'}), 200


@app.errorhandler(Exception)
def handle_exception(error):
    return ExceptionHandler.handle_exception(error)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
