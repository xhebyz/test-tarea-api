from graphene import ObjectType, String, Schema, ID, Field
import graphene
from logic.tarea import TareaLogic
from database.mongo import MongoDB
from data.objects import Tarea

db = MongoDB()
tarea_logic = TareaLogic(db)

class TareaQL(ObjectType):
    id = ID()
    titulo = String()
    descripcion = String()
    estado = String()
    fecha_vencimiento = String()


class TareaInput(graphene.InputObjectType):
    id = graphene.Int(required=True)
    titulo = graphene.String(required=True)
    descripcion = graphene.String(required=True)
    estado = graphene.String(required=True)
    fecha_vencimiento = graphene.String(required=True)


class Query(graphene.ObjectType):
    tarea = graphene.Field(TareaQL, id=graphene.ID(required=True))
    todas_las_tareas = graphene.List(TareaQL)

    def resolve_todas_las_tareas(self, info):
        tareas = tarea_logic.get_all_tareas()
        return tareas

    def resolve_tarea(self, info, id):
        tarea = tarea_logic.get_tarea_id(id)
        return tarea


class CrearTarea(graphene.Mutation):
    class Arguments:
        input = TareaInput(required=True)

    tarea = graphene.Field(TareaQL)

    def mutate(self, info, input):
        tarea_insert = Tarea(
            id=None,
            titulo=input.titulo,
            descripcion=input.descripcion,
            estado=input.estado,
            fecha_vencimiento=input.fecha_vencimiento
        )
        tarea_insert.validate()
        tarea_id = tarea_logic.add_tarea(tarea_insert.to_dict())
        tarea_insert._id = str(tarea_id)
        # Guarda la tarea en la base de datos o donde sea que estés almacenando los datos
        input.id = tarea_id
        return CrearTarea(tarea_insert.to_dict_res())

class ActualizarTarea(graphene.Mutation):
    class Arguments:
        input = TareaInput(required=True)

    tarea = graphene.Field(TareaQL)

    def mutate(self, info, input):

        tarea_id = input.id
        tarea_update = Tarea(
            id=tarea_id,
            titulo=input.titulo,
            descripcion=input.descripcion,
            estado=input.estado,
            fecha_vencimiento=input.fecha_vencimiento
        )
        tarea_update.validate()
        tarea_logic.update_tarea(tarea_id, tarea_update.to_dict())
        return ActualizarTarea(tarea=tarea_update.to_dict_res())


class EliminarTarea(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        # Lógica para eliminar una tarea por ID
        # Implementa la lógica para eliminar la tarea de la base de datos o donde sea que desees
        pass


class Mutaciones(graphene.ObjectType):
    crear_tarea = CrearTarea.Field()
    actualizar_tarea = ActualizarTarea.Field()
    eliminar_tarea = EliminarTarea.Field()


schema = graphene.Schema(query=Query, mutation=Mutaciones)
