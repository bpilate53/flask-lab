import pymongo

class Database:

    def get_database(self):
        # db_client = pymongo.MongoClient('localhost', 27017)
        db_client = pymongo.MongoClient('mongodb+srv://admin:tetCoZtfl6JS3pbt@cluster0.eojsgnw.mongodb.net/?retryWrites=true&w=majority')
        
        todo_db = db_client.todo_db

        return todo_db