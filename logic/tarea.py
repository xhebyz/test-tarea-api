from bson import ObjectId
from exceptions.error import NotFoundException, CustomException
from pymongo.collection import ReturnDocument

class TareaLogic:
    def __init__(self, db):
        self.db = db

    def get_all_tareas(self):
        tasks_collection = self.db.get_collection('tareas')
        tareas = list(tasks_collection.find())

        for tarea in tareas:
            tarea['_id'] = str(tarea['_id'])
            tarea['id'] = str(tarea['_id'])

        return tareas

    def get_tarea_id(self, tarea_id):
        tasks_collection = self.db.get_collection('tareas')
        tarea = tasks_collection.find_one({'_id': tarea_id})

        if not tarea:
            raise NotFoundException()

        return tarea

    def add_tarea(self, tarea_data):
        tasks_collection = self.db.get_collection('tareas')

        contador = tasks_collection.counters.find_one_and_update(
            {'_id': 'tarea_id'},
            {'$inc': {'seq': 1}},
            projection={'seq': True, '_id': False},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        tarea_id = contador['seq']
        tarea_data['_id'] = tarea_id

        tarea_id = tasks_collection.insert_one(tarea_data).inserted_id
        return tarea_id

    def update_tarea(self, tarea_id, tarea_data):
        tasks_collection = self.db.get_collection('tareas')
        res = tasks_collection.update_one({'_id': tarea_id}, {'$set': tarea_data})

        if res.modified_count <= 0:
            raise CustomException(500, "No se a actualizado ningun objeto")

    def eliminar_tarea(self, tarea_id):
        tasks_collection = self.db.get_collection('tareas')
        res = tasks_collection.delete_one({'_id': tarea_id})

        if res.deleted_count <= 0:
            raise NotFoundException()
