from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()

class Workout(db.Model):
    __tablename__= 'workout'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dia = Column(String(80))
    treino = Column(String(80))
    duracao = Column(String(80))

    def to_json(self):
        return {'id': str(self.id),
        'dia': str(self.dia),
        'treino': str(self.treino),
        'duracao': str(self.duracao)
        }

def connect_db(app):
    db.app = app  
    db.init_app(app)
    db.create_all()

