from src.config.db_config import connection



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
            return student
        except Exception as e:
            print("Could not connect to the database: ", e)


