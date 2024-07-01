from src import app
from flask import jsonify
from src.controllers.student import Controller_estudiante

controller = Controller_estudiante()

@app.route('/estudiante',methods=['GET'])
def get_student():
    students = controller.get_student()
    return jsonify (students)

@app.route('/estudiante',methods=['POST'])
def create_student():
    return jsonify({'message':'Hello, World'})

@app.route('/estudiante',methods=['PUT'])
def update_student():
    return jsonify({'message':'Hello, World'})

@app.route('/estudiante',methods=['DELETE'])
def delete_student():
    return jsonify({'message':'Hello, World'})