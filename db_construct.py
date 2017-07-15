from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def __repr__(self):
        return '<Name %r>' % self.name
    
"""
db.create_all()
user = User('John Doe', 'john.doe@example.com')
db.session.add(user)
db.session.commit()
"""