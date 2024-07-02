from src import app
from flask import jsonify,request
from src.controllers.student import Controller_estudiante

controller = Controller_estudiante()
student = []
 
@app.route('/student',methods=['GET']) # GET /student is used to get all the students
def get_student():
    students = controller.get_student() # get the students
    return jsonify (students)

@app.route('/student',methods=['POST']) # POST is used to create a new data
def create_student():
    data = request.get_json(force=True) # request.get_json(force=True) is used to get the data from the request body
    res = controller.create_student(data)
    return res

@app.route('/student',methods=['PUT']) # PUT is used to update the data
def update_student():
    data = request.get_json(force=True) # request.get_json(force=True) is used to get the data from the request body
    res = controller.update_student(data)
    return res

@app.route('/student/<id>',methods=['DELETE']) # DELETE is used to delete the data
def delete_student(id):
    res = controller.delete_student(id)
    return res