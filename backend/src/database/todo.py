from . import db
from sqlalchemy import or_
import app

class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String)
    owner = db.Column(db.String) # UUID
    shared = db.Column(db.String) # UUID

class TodoDAO(object): # DAO = Data Access Object
    def __init__(self, session):
        self.session = session

    def todos(self, id=None):
        """Get all todos, or a specific one if id is given. This is for Administrators"""
        app.logger.info(f"ToDo-DB: Admin requested " + ("a list of all ToDos" if id is None else f"ToDo {id}") )
        q = self.session.query(TodoModel)

        if id is None:
            return q.all()

        # id is given
        if todo:=q.filter_by(id=id).first():
            return todo
        else:
            return None # Todo not found
            

    def todos_access_filtered(self, owner, groups, id=None):
        """Get all the todos *a user has access to*, or a specific one if id is given"""
        app.logger.info(f"ToDo-DB: User or developer requested " + ("a list of all ToDos" if id is None else f"ToDo {id}") )
        q = self.session.query(TodoModel).filter(or_(
            TodoModel.owner==owner, # Is owner of this todo
            or_(TodoModel.shared == grp for grp in groups)) # Is in one of the groups this todo is shared with
        )

        if id is None:
            return q.all()

        # id is given
        if todo:=q.filter_by(id=id).first():
            return todo
        else:
            return None # Todo not found

    def create(self, task, owner, shared):
        """Create a new todo in the database"""
        app.logger.info(f"ToDo-DB: Creating ToDo: {str(task)}")
        todo = TodoModel(task=task, owner=owner, shared=shared)
        self.session.add( todo )
        self.session.commit()
        return todo

    def update(self, id, data):
        """Change any todo. This is for Administrators"""
        app.logger.info(f"ToDo-DB: Admin is updating ToDo {id}: {data}")
        if (todo:=self.todos(id=id)) is not None:
            # "data" is a dictionary of key:value pairs to be upated. Update the respective attributes of the todo
            # through "setattr". Updates are allowed for the "task", "shared" and "owner" properties
            [setattr(todo, key, val) for key, val in data.items() if key in ["task", "shared", "owner"]]
            self.session.commit()
            return todo
        else:
            return None

    def update_access_filtered(self, owner, groups, id, data):
        app.logger.info(f"ToDo-DB: User or developer is updating ToDo {id}: {data}")
        """Change a todo the user has access to"""
        if (todo:=self.todos_access_filtered(owner=owner, groups=groups, id=id)) is not None:
            [setattr(todo, key, val) for key, val in data.items() if key in ["task", "shared", "owner"]]
            self.session.commit()
            return todo
        else:
            return None

    def delete(self, id):
        """Delete any Todo. This is for Administrators"""
        app.logger.info(f"ToDo-DB: Administrator deletes ToDo {id}")
        if todo:=self.todos(id=id):
            self.session.delete(todo)
            self.session.commit()
            return id
        else:
            return None

    def delete_access_filtered(self, owner, groups, id):
        """Delete any Todo. This is for non-Admins"""
        app.logger.info(f"ToDo-DB: User or developer deletes ToDo {id}")
        if todo:=self.todos_access_filtered(owner=owner, groups=groups, id=id):
            self.session.delete(todo)
            self.session.commit()
            return id
        else:
            return None