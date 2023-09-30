# Documentación de GraphQL

Esta documentación proporciona una guía detallada de las operaciones GraphQL disponibles en este sistema. GraphQL es un lenguaje de consulta para API que permite a los clientes solicitar datos específicos que necesitan. A continuación, se describen las consultas y mutaciones que puedes realizar en este servidor GraphQL.

## **Mutación: Obtener Token de Acceso**

Esta mutación te permite obtener un token de acceso para autenticarte en el sistema.

```graphql
mutation GetAccessToken {
    getAccessToken(password: "passs===", userId: "admin") {
        accessToken
    }
}
```

### **Parámetros**

- `password`: Contraseña del usuario.
- `userId`: Identificación del usuario.

### **Respuesta**

- `accessToken`: Token de acceso que se utilizará en las operaciones autenticadas.

---

## **Consulta: Obtener Todas las Tareas**

Esta consulta devuelve todas las tareas disponibles en el sistema.

```graphql
query AllTasks {
    allTasks {
        id
        title
        description
        status
        dueDate
    }
}
```

### **Respuesta**

- `id`: Identificador único de la tarea.
- `title`: Título de la tarea.
- `description`: Descripción de la tarea.
- `status`: Estado actual de la tarea.
- `dueDate`: Fecha de vencimiento de la tarea.

---

## **Consulta: Obtener Detalles de una Tarea**

Esta consulta devuelve los detalles de una tarea específica según su ID.

```graphql
query Task {
    task(id: null) {
        id
        title
        description
        status
        dueDate
    }
}
```

### **Parámetros**

- `id`: Identificador único de la tarea que se desea obtener.

### **Respuesta**

- `id`: Identificador único de la tarea.
- `title`: Título de la tarea.
- `description`: Descripción de la tarea.
- `status`: Estado actual de la tarea.
- `dueDate`: Fecha de vencimiento de la tarea.

---

## **Mutación: Crear una Nueva Tarea**

Esta mutación te permite crear una nueva tarea en el sistema.

```graphql
mutation CreateTask {
    createTask(
        input: {
            id: null
            title: "Postman"
            description: "Describe"
            status: "En proceso"
            dueDate: "2019-01-01 01:00:00"
        }
    ) {
        task {
            id
            title
            description
            status
            dueDate
        }
    }
}
```

### **Parámetros**

- `id`: Identificador único de la nueva tarea (puede ser null para generarse automáticamente).
- `title`: Título de la nueva tarea.
- `description`: Descripción de la nueva tarea.
- `status`: Estado inicial de la nueva tarea.
- `dueDate`: Fecha de vencimiento de la nueva tarea.

### **Respuesta**

- `id`: Identificador único de la tarea creada.
- `title`: Título de la tarea.
- `description`: Descripción de la tarea.
- `status`: Estado actual de la tarea.
- `dueDate`: Fecha de vencimiento de la tarea.

---

## **Mutación: Actualizar Tarea**

Esta mutación permite actualizar los detalles de una tarea existente en el sistema.

```graphql
mutation UpdateTask {
    updateTask(
        input: {
            id: 29
            title: "Esta sí"
            description: "Postman"
            status: "En proceso"
            dueDate: "1987-01-01 02:00:00"
        }
    ) {
        task {
            id
            title
            description
            status
            dueDate
        }
    }
}
```

### **Parámetros**

- `id`: Identificador único de la tarea que se desea actualizar.
- `title`: Nuevo título de la tarea.
- `description`: Nueva descripción de la tarea.
- `status`: Nuevo estado de la tarea.
- `dueDate`: Nueva fecha de vencimiento de la tarea.

### **Respuesta**

- `id`: Identificador único de la tarea actualizada.
- `title`: Título actualizado de la tarea.
- `description`: Descripción actualizada de la tarea.
- `status`: Estado actualizado de la tarea.
- `dueDate`: Fecha de vencimiento actualizada de la tarea.

---

## **Mutación: Eliminar Tarea**

Esta mutación te permite eliminar una tarea del sistema.

```graphql
mutation DeleteTask {
    deleteTask(id: 30) {
        success
    }
}
```

### **Parámetros**

- `id`: Identificador único de la tarea que se desea eliminar.

### **Respuesta**

- `success`: Indica si la operación de eliminación fue exitosa (`true`) o no (`false`).

---

Recuerda que estas son las operaciones GraphQL disponibles en este sistema. Utiliza el token de acceso obtenido mediante la mutación `GetAccessToken` para realizar operaciones autenticadas.