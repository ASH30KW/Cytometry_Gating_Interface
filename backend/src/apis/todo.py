from operator import imod
from flask_restx import Namespace, Resource, fields
from cp_utils.auth import withTokenOnly, authorizations
import app


TodoDAO = app.database.TodoDAO

api = Namespace('todos', description='TODO operations', authorizations=authorizations)

TodoApiModel = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details'),
    'shared': fields.String(required=False, description='Group UUID this Todo is shared with'),
    'owner': fields.String(required=True, description='UUID of the user who is the owner of the Todo'),
})

@api.route('/')
class TodoList(Resource):
    '''Shows a list of all ToDos, and lets you POST to add new ToDos'''
    @withTokenOnly(api)
    @api.doc('list_todos')
    @api.marshal_list_with(TodoApiModel)
    def get(self):
        '''List all todos for you'''
        app.logger.info(f"ToDo-API: {api.current_user['role']} {api.current_user['name']} requests a list of all ToDos")
        if api.current_user["role"] == "admin": # Admins can see all todos
            return TodoDAO.todos()
        else:
            return TodoDAO.todos_access_filtered(
                owner=api.current_user["uuid"],
                groups=api.current_user["groups"]
                )

    @withTokenOnly(api)
    @api.doc('create_todo')
    @api.expect(TodoApiModel)
    @api.marshal_with(TodoApiModel, code=201)
    def post(self):
        '''Create a new ToDo'''
        app.logger.info(f"ToDo-API: {api.current_user['role']} {api.current_user['name']} creates a new ToDo: \"{api.payload['task']}\"")
        return TodoDAO.create(
            task=api.payload["task"]+" :)",
            owner=api.current_user["uuid"],
            shared=api.payload["shared"]
            ), 201


@api.route('/<int:id>')
@api.response(404, 'Todo not found')
@api.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single ToDo item and lets you delete them'''
    @withTokenOnly(api)
    @api.doc('get_todo')
    @api.marshal_with(TodoApiModel)
    def get(self, id):
        '''Fetch a given ToDo by id'''
        app.logger.info(f"ToDo-API: {api.current_user['role']} {api.current_user['name']} fetches ToDo {id}")
        todo = None

        if api.current_user["role"]=="admin":
            todo = TodoDAO.todos(id=id)
        else:
            todo = TodoDAO.todos_access_filtered(
                owner=api.current_user["uuid"],
                groups=api.current_user["groups"],
                id=id
                )

        if todo is None:
            api.abort(404, "Todo {} not found".format(id))
        else:
            return todo

    @withTokenOnly(api)
    @api.doc('delete_todo')
    @api.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a ToDo given its id'''
        app.logger.info(f"ToDo-API: {api.current_user['role']} {api.current_user['name']} deletes ToDo {id}")
        del_id = None

        if api.current_user["role"]=="admin":
            del_id = TodoDAO.delete(id=id)
        else:
            del_id = TodoDAO.delete_access_filtered(
                owner=api.current_user["uuid"],
                groups=api.current_user["groups"],
                id=id
                )

        if del_id==id is None:
            return f"Deleted Todo {id}", 204
        else:
            api.abort(404, "Todo {} not found".format(id))

    @withTokenOnly(api)
    @api.expect(TodoApiModel)
    @api.marshal_with(TodoApiModel)
    def put(self, id):
        '''Update a Todo given its id'''
        app.logger.info(f"ToDo-API: {api.current_user['role']} {api.current_user['name']} updates ToDo {id}")
        todo = None

        if api.current_user["role"]=="admin":
            todo = TodoDAO.update(id=id, data=api.payload)
        else:
            todo = TodoDAO.update_access_filtered(
                owner=api.current_user["uuid"],
                groups=api.current_user["groups"],
                id=id,
                data=api.payload
                )

        if todo is None:
            api.abort(404, f"Todo {id} not found")
        else:
            return todo