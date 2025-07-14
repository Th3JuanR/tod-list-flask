from todor import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    # Para manipular los datos (constructor)
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def __repr__(self):
        return f'<user:{self.username}>'
    
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    state = db.Column(db.Boolean, default=False)
    
    # Para manipular los datos (constructor)
    def __init__(self, create_by, title, desc, state = None):
        self.create_by = create_by
        self.title = title
        self.desc = desc
        self.state = state  # Corregido: self.state
    def __repr__(self):
        return f'<Todo: {self.title}>'