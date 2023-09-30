from bson import ObjectId
from flask import jsonify
from exceptions.error import NotFoundException


class TareaLogic:
    def __init__(self, db):
        self.db = db

    def get_all_tareas(self):
        tasks_collection = self.db.get_collection('tareas')
        tareas = list(tasks_collection.find())

        for tarea in tareas:
            tarea['_id'] = str(tarea['_id'])

        return tareas

    def get_tarea_id(self, tarea_id):
        tasks_collection = self.db.get_collection('tareas')
        tarea = tasks_collection.find_one({'_id': ObjectId(tarea_id)})

        if tarea:
            tarea['_id'] = str(tarea['_id'])

        return tarea

    def add_tarea(self, tarea_data):
        tasks_collection = self.db.get_collection('tareas')
        tarea_id = tasks_collection.insert_one(tarea_data).inserted_id
        return tarea_id

    def update_tarea(self, tarea_id, tarea_data):
        tasks_collection = self.db.get_collection('tareas')
        res = tasks_collection.update_one({'_id': ObjectId(tarea_id)}, {'$set': tarea_data})

        if res.modified_count <= 0:
            raise NotFoundException()

    def eliminar_tarea(self, tarea_id):
        tasks_collection = self.db.get_collection('tareas')
        res = tasks_collection.delete_one({'_id': ObjectId(tarea_id)})

        if res.deleted_count <= 0:
            raise NotFoundException()
