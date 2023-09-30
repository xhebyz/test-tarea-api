# Test CRUD Tareas

Este proyecto implementa un sistema CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar tareas utilizando Flask y MongoDB. Las operaciones pueden ser realizadas tanto a través de una API REST como con GraphQL.

## Requisitos Previos

- Asegúrate de tener Python 3.8 o superior instalado en tu sistema.
- MongoDB debe estar instalado y en funcionamiento en el puerto predeterminado (27017).

## Configuración del Entorno Virtual (Opcional pero Recomendado)

```bash
# Instalar virtualenv si aún no está instalado
pip install virtualenv

# Crear un entorno virtual
virtualenv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS y Linux:
source venv/bin/activate
```

## Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/test-crud-tareas.git
```

### 2. Navegar al Directorio del Proyecto
```bash
cd test-crud-tareas
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configuración de la Base de Datos
- Crea una base de datos MongoDB llamada "test_crud_tareas".
- Configura las credenciales de MongoDB en un archivo `.env` en el directorio del proyecto:

```env
MONGO_URI=
DEBUG=
JWT_SECRET=
USER_ADMIN=
HASH_ACCESS=
```

### 5. Ejecutar la Aplicación
```bash
# Iniciar el servidor Flask
python app.py
```

La aplicación estará disponible en http://localhost:5000.

## Documentación de Servicios

- Documentación [API REST - Postman](https://documenter.getpostman.com/view/4357888/2s9YJaZ4V6)
- Documentación [GraphQL](docs/GraphQL.md)

---

Desarrollado y diseñado por Sebastián Araos - 2023