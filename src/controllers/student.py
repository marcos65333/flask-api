from src.models.student import Student

class Controller_estudiante():
    
    def __init__(self):
        self.student = Student()
        
    def get_student(self):
       try:
           return self.student.get_students()
       except Exception as e:
           print("Error",e)