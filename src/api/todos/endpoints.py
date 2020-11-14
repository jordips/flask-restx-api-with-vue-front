from flask import jsonify
from flask_restx import Namespace, Resource, fields
import json
from random import randint

from .models import todo_model

ns = Namespace('todos', description='Todos operations')

# Add models
ns.add_model("todo", todo_model)

# Init Array
todos = [
    {'id': '123', 'task': 'Clean the bedroom'},
    {'id': '563', 'task': 'Go to shop milk'}
]

@ns.route("/")
class TodoList(Resource):
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo_model)
    def get(self):
        """
        Returns a list of todos
        """
        return todos

    @ns.doc('create_todo')
    @ns.expect(todo_model)
    @ns.marshal_with(todo_model, code=201)
    def post(self):
        """
        Adds a new todo to the list
        """
        todo = ns.payload
        todo['id'] = randint(0, 1000)
        todos.append(todo)
        return todo

@ns.route("/<int:id>")
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):

    @ns.doc('get_todo')
    @ns.marshal_with(todo_model)
    def get(self, id):
        '''Fetch a given resource'''
        for todo in todos:
            if todo['id'] == id:
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        for todo in todos:
            if todo['id'] == id:
                todos.remove(todo)
                return '', 204
        api.abort(404, "Todo {} doesn't exist".format(id))

    @ns.expect(todo_model)
    @ns.marshal_with(todo_model)
    def put(self, id):
        '''Update a task given its identifier'''
        for todo in todos:
            if todo['id'] == id:
                todo.update(ns.payload)
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))
