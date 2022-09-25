from http import client
from flask import Flask, render_template
import os
import pymongo
from todo import routes

app = Flask(__name__, instance_relative_config=True)

# routes of our application
app.register_blueprint(routes.bp)

# # registering a database
# mongo_client = pymongo.MongoClient('localhost', 27017)
# todo_db = mongo_client.todo_db

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)
