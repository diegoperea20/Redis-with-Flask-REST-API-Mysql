from flask import jsonify, request
from app import app, db, redis_client
from models import Task, task_schema, tasks_schema
import  json 
from json import loads, dumps

@app.route("/tasks", methods=["POST"])
def create_task():
    title = request.json["title"]
    description = request.json["description"]

    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Obtener todas las tareas desde Redis
    cached_tasks = redis_client.lrange('tasks', 0, -1)

    if cached_tasks:
        # Si están en caché, devuelve las tareas desde Redis
        tasks = [json.loads(task.decode('utf-8')) for task in cached_tasks]
        #print("Tareas recuperadas de la caché en Redis:", tasks)
        return jsonify(tasks)

    # Si no están en caché, obtén todas las tareas de la base de datos
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks)

    # Almacena las tareas en Redis como elementos individuales en una lista
    for task in result:
        redis_client.rpush('tasks', json.dumps(task, default=str))

    #print("Tareas almacenadas en Redis:", result)

    return jsonify(result)



@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    # Intenta obtener la tarea desde Redis
    task_cache_key = f'task:{id}'
    cached_task = redis_client.get(task_cache_key)

    if cached_task:
        # Si está en caché, devuelve la tarea desde Redis
        return jsonify(loads(cached_task))

    # Si no está en caché, obtén la tarea de la base de datos
    task = Task.query.get(id)

    if task:
        # Almacena la tarea en Redis para futuras consultas
        redis_client.set(task_cache_key, dumps(task_schema.dump(task)))
        return jsonify(task_schema.dump(task))
    else:
        return jsonify({"message": "Tarea no encontrada"}), 404



@app.route("/tasks/<id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get(id)
    title = request.json["title"]
    description = request.json["description"]

    task.title = title
    task.description = description
    db.session.commit()
    return task_schema.jsonify(task)


@app.route("/tasks/<id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)
