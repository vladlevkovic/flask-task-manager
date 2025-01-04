from flask import Flask
from flask_restful import Api, Resource, reqparse
from db import create_task, get_all_tasks, task_complete

app = Flask(__name__)
api = Api(app)

class TaskManager(Resource):
    def get(self):
        tasks = get_all_tasks()
        print(tasks)
        tasks_dict = {}
        for i in range(len(tasks)):
            tasks_dict[tasks[i][0]] = {
                'title': tasks[i][1],
                'description': tasks[i][2],
                'completed': False if tasks[i][3] == 0 else True
            }
        return tasks_dict

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('description')
        params = parser.parse_args()
        create_task(params['title'], params['description'])
        return {'message': 'Задачу створено'}

    def put(self, task_id):
        parser = reqparse.RequestParser()
        parser.add_argument('complete')
        params = parser.parse_args()
        task_complete(task_id, params['complete'])
        return {'message': 'Задачу виконано'}

    def delete(self):
        pass

api.add_resource(TaskManager, '/api/v1/tasks', '/api/v1/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
