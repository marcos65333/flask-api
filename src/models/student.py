from src.config.db_config import connection
from flask import jsonify


class Student:
    
    def __init__(self):
        self.conn = connection()
    
    def get_students(self):
        try:
            conn = connection()
            cursor = conn.cursor()
            sql ="SELECT * FROM estudiante"
            cursor.execute(sql)
            student = []
            for row in cursor:
                student.append({
                    'id': row[0],
                    'nombre': row[1],
                    'apellido': row[2],
                    'correo': row[3]
                })
            return student
        except Exception as e:
            print("Could not connect to the database: ", e)


    def create_student(self, data):
        try:
            if self.verify_if_student_exits_by_email(data):
                return ({'message': 'Student already exists'}),401
            conn = connection()
            cursor = conn.cursor()
            sql = "INSERT INTO estudiante (nombre, apellido, correo) VALUES (%s, %s, %s)"
            cursor.execute(sql, (data['nombre'], data['apellido'], data['correo']))
            conn.commit()
            return jsonify({'message': 'Student created successfully'}),201
        except Exception as e:
            print("Could not connect to the database: ", e)
            
    def verify_if_student_exits_by_email(self,data):
        try:
            conn = connection()
            cursor = conn.cursor()
            sql ="SELECT * FROM estudiante WHERE correo = %s"
            cursor.execute(sql,(data['correo'],))
            for i in cursor:
                if i[3] == data['correo']:
                    return True
            return False
        except Exception as e:
            print("Could not connect to the database: ", e)
    
    def verify_if_student_exits_by_id(self,id):
        try:
            conn = connection()
            cursor = conn.cursor()
            sql ="SELECT * FROM estudiante WHERE id = %s"
            cursor.execute(sql,(id,))
            for i in cursor:
                if i[0] == int(id):
                    return True
            return False
        except Exception as e:
            print("Could not connect to the database: ", e)  
                
    def update_student(self,data):
        try:
            if self.verify_if_student_exits_by_id(data) == False:
                return jsonify({'message': 'Student does not exist'}),404
            conn = connection() #create variable conexion
            cursor = conn.cursor() #create variable cursor
            sql = "UPDATE estudiante SET nombre=%s, apellido=%s WHERE correo=%s" #create sql sentence
            cursor.execute(sql, (data['nombre'], data['apellido'], data['correo']))  #execute sql sentence
            conn.commit() #commit changes
            return jsonify({'message': 'Student updated successfully'}),200
        except Exception as ex:
            print("Could not connect to the database: ", ex)
            
    def delete_student(self,id):
        try:
            if self.verify_if_student_exits_by_id(id) == False:
                return jsonify({'message': 'Student does not exist'}),404
            conn = connection() #create variable
            cursor = conn.cursor() #create variable cursor
            sql = "DELETE FROM estudiante WHERE id=%s" #create sql sentence
            cursor.execute(sql,(id,)) #execute sql sentence
            conn.commit() #commit changes
            return jsonify({'message': 'Student deleted successfully'}),200
        except Exception as e:
            print("Could not connect to the database: ", e)