from datetime import datetime

ESTADOS_PERMITIDOS = ['pendiente', 'en progreso', 'completada', 'cancelada']
FORMATE_DATETIME = '%Y-%m-%d %H:%M:%S'


class ObjectData:

    def validate(self, required=None):
        res = []
        if required is None:
            required = []
        for att in required:
            if not hasattr(self, att) or getattr(self, att) is None:
                res.append(str(att))
        return res


class Tarea(ObjectData):
    def __init__(self, id, titulo, descripcion, estado, fecha_vencimiento):
        self._id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, FORMATE_DATETIME)

    @staticmethod
    def dict_to_obj(data: dict):
        tarea = Tarea(
            id=data.get("_id"),
            titulo=data.get("titulo"),
            descripcion=data.get("descripcion"),
            estado=data.get("estado"),
            fecha_vencimiento=data.get("fecha_vencimiento"),

        )
        return tarea

    def validate_estado(self):
        if self.estado not in ESTADOS_PERMITIDOS:
            raise ValueError(f'Estado no válido. Estados permitidos: {", ".join(ESTADOS_PERMITIDOS)}')

    def validation_data(self):
        res = self.validate(["titulo", "descripcion", "estado", "fecha_vencimiento"])
        if len(res) != 0:
            raise ValueError(f'Campos Requeridos : {", ".join(res)}')
        self.validate_estado()

    def to_dict(self):
        return {
            '_id': self._id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'estado': self.estado,
            'fecha_vencimiento': self.fecha_vencimiento.strftime(FORMATE_DATETIME)
        }

    def to_dict_res(self):
        return {
            'id': self._id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'estado': self.estado,
            'fecha_vencimiento': self.fecha_vencimiento.strftime(FORMATE_DATETIME)
        }

    @staticmethod
    def from_dict(data):
        tarea = Tarea(id=None, titulo=data['titulo'], descripcion=data['descripcion'], estado=data['estado'], fecha_vencimiento=data['fecha_vencimiento'])
        tarea.validation_data()
        return tarea
