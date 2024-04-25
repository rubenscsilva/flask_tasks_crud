from flask import Flask, request, jsonify
from models.tasks import Task

app = Flask(__name__)

#CRUD : Create, Read, Update and Delete

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def created_task():
    global task_id_control
    data = request.get_json()
    # new_task = Task(id=task_id_control, title=data.get('title'), description=data.get('description', ''))
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ''))
    task_id_control +=1
    tasks.append(new_task)
    print(tasks)
    return jsonify({'message': 'Nova tarefa criada com sucesso'})

if __name__ == "__main__":
    app.run(debug=True)