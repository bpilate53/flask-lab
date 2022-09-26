from random import random
import uuid
from flask import Flask, jsonify, request
from db import Database

class Task:
    def __init__(self):
        self.todo_db = Database().get_database()

    def create(self):
        # print(request.form)
        task = {
            "name": request.form.get('taskname'),
            "user_id": ""
        }

        # task = {
        #     "name": "task" + uuid.uuid4().hex,
        #     "user_id": ""
        # }

        # check for existing task
        try: 
            self.todo_db.tasks.insert_one(task)
        except:
            return {'error': 'Cannot delete.'}
        else:
            return {'error': 'Cannot delete.'}

        return {'error': 'Cannot delete.'}
        
    def update(self):
        update_task_name = request.form.get('taskname')
        if update_task_name:
            try:
                self.todo_db.tasks.update_one({'name':request.form.get('oldname')}, {'$set': {'name': update_task_name}})
                return self.get_one(update_task_name)
            except:
                return {'error': 'cannot update'}
        else:
            return {'error': 'cannot update'}
    
    def delete(self, name):
        task_exist = self.task_exist(name)

        if task_exist:
            try:
                self.todo_db.tasks.delete_one({'name': name})
            except:
                return {'error': 'Cannot delete.'}
            else:
                return {'error': 'Cannot delete.'}
            
        return {'error': 'Cannot delete.'}

    def get_all(self):
            all_tasks = self.todo_db.tasks.find({})
            if all_tasks:
                return list(all_tasks)
            else:
                return {'error': 'No tasks available'}
    
    def get_one(self, name):
        task = list(self.todo_db.tasks.find({'name': name}))

        if len(list(task)) > 0:
            return (list(task))[0]
        return {'error': 'No task found'}
    
    def task_exist(self, name):
        task_exist = self.get_one(name)

        if 'error' in task_exist:
            return False
        return True
            