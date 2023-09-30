# Test CRUD Tareas

Este proyecto implementa un CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar tareas usando Flask y MongoDB.

## Requisitos Previos

- Python 3.6 o superior instalado en tu sistema.
- MongoDB instalado y en funcionamiento en el puerto predeterminado (27017).

## Configuración del Entorno Virtual (Opcional pero Recomendado)

```bash
# Instalar virtualenv si no está instalado
pip install virtualenv

# Crear un entorno virtual
virtualenv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS y Linux:
source venv/bin/activate
```

Instalación

# Clonar el repositorio
git clone https://github.com/tu-usuario/test-crud-tareas.git

# Ir al directorio del proyecto
cd test-crud-tareas

# Instalar dependencias
pip install -r requirements.txt



Configuración de la Base de Datos

    Crea una base de datos MongoDB llamada "test_crud_tareas".
    Configura las credenciales de MongoDB en un archivo .env en el directorio del proyecto:

ini

MONGO_URI=mongodb://usuario:password@localhost:27017/test_crud_tareas

Ejecutar la Aplicación

bash

# Iniciar el servidor Flask
python app.py

La aplicación estará disponible en http://localhost:5000.
Uso

    GET /tareas: Obtener todas las tareas.
    GET /tareas/<id>: Obtener una tarea por su ID.
    POST /tareas: Crear una nueva tarea.
    PUT /tareas/<id>: Actualizar una tarea existente.
    DELETE /tareas/<id>: Eliminar una tarea por su ID.

Ejemplos de Solicitudes

    Crear una tarea:

    http

POST /tareas
Content-Type: application/json

{
  "titulo": "Tarea de ejemplo",
  "descripcion": "Descripción de la tarea",
  "estado": "pendiente",
  "fecha_vencimiento": "2023-12-31"
}

Actualizar una tarea:

http

PUT /tareas/<id>
Content-Type: application/json

{
  "estado": "completada"
}

Eliminar una tarea:

http

    DELETE /tareas/<id>

