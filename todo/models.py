from urllib import request
import uuid
from flask import Flask, jsonify
from db import Database

class Task:
    def __init__(self):
        self.todo_db = Database().get_database()

    def create(self):
        # print(request.form)
        # task = {
        #     "_id" : uuid.uuid4().hex,
        #     "name": request.form.get('name'),
        #     "user_id": ""
        # }

        task = {
            "name": "request.form.get('name')",
            "user_id": ""
        }

        self.todo_db.tasks.insert_one(task)

        return jsonify(task), 200

