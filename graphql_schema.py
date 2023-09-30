from graphene import ObjectType, String, Schema, ID, Field
import graphene

from auth.jwt import create_token, verify_user
from logic.tarea import TareaLogic
from database.mongo import MongoDB
from data.objects import Tarea
from flask_jwt_extended import jwt_required

db = MongoDB()
tarea_logic = TareaLogic(db)

class TareaQL(ObjectType):
    id = ID()
    titulo = String()
    descripcion = String()
    estado = String()
    fecha_vencimiento = String()


class TareaInput(graphene.InputObjectType):
    id = graphene.Int(required=False)
    titulo = graphene.String(required=True)
    descripcion = graphene.String(required=True)
    estado = graphene.String(required=True)
    fecha_vencimiento = graphene.String(required=True)


class Query(graphene.ObjectType):

    tarea = graphene.Field(TareaQL, id=graphene.Int(required=True))
    all_tareas = graphene.List(TareaQL)

    @jwt_required()
    def resolve_all_tareas(self, info):
        tareas = tarea_logic.get_all_tareas()
        return tareas

    @jwt_required()
    def resolve_tarea(self, info, id):
        res = tarea_logic.get_tarea_id(id)
        return Tarea.dict_to_obj(res).to_dict_res()


class CreateTarea(graphene.Mutation):
    class Arguments:
        input = TareaInput(required=True)

    tarea = graphene.Field(TareaQL)

    @jwt_required()
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
        return CreateTarea(tarea = tarea_insert.to_dict_res())

class UpdateTarea(graphene.Mutation):
    class Arguments:
        input = TareaInput(required=True)

    tarea = graphene.Field(TareaQL)

    @jwt_required()
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
        return UpdateTarea(tarea=tarea_update.to_dict_res())


class DeleteTarea(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    @jwt_required()
    def mutate(self, info, id):
        tarea_logic.eliminar_tarea(tarea_id=id)
        return DeleteTarea(success=True)


class GetTokenAcess(graphene.Mutation):
    class Arguments:
        user_id = graphene.String(required=True)
        password = graphene.String(required=True)

    access_token = graphene.String()

    def mutate(self, info, user_id, password):
        access_token = create_token(user_id, password)
        return GetTokenAcess(access_token)


class Mutaciones(graphene.ObjectType):
    create_tarea = CreateTarea.Field()
    update_tarea = UpdateTarea.Field()
    delete_tarea = DeleteTarea.Field()
    get_acces_token = GetTokenAcess.Field()


schema = graphene.Schema(query=Query, mutation=Mutaciones)
