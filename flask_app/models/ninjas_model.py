from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash



class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_ninjas(cls):
        query = """
                SELECT * FROM ninjas;
                """
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_ninjas = []
        for row_from_db in results:
            ninja_instance = cls(row_from_db)
            all_ninjas.append(ninja_instance)
        return all_ninjas
        
    @classmethod
    def get_ninjas_by_dojo(cls, id):
        query = """
                SELECT * FROM ninjas
                WHERE dojo_id=%(id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query)
        all_ninjas = []
        for row_from_db in results:
            ninja_instance = cls(row_from_db)
            all_ninjas.append(ninja_instance)
        return all_ninjas
    
    @classmethod
    def create(cls,data):
        query = """
                INSERT INTO ninjas (first_name, last_name, age, dojo_id)
                VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
                """
        return connectToMySQL(DATABASE).query_db(query,data)
    