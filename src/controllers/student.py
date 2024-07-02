from src.models.student import Student

class Controller_estudiante():
    
    def __init__(self):
        self.student = Student()
        
    def get_student(self):
       try:
           return self.student.get_students()
       except Exception as e:
           print("Error",e)
    
    def create_student(self, data):
        try:
            return self.student.create_student(data)
        except Exception as e:
            print("Error",e)
    
    def update_student(self,data):
        try:
            return self.student.update_student(data)
        except Exception as e:
            print("Error",e)
            
    def delete_student(self,id):
        try:
            return self.student.delete_student(id)
        except Exception as e:
            print("Error",e)