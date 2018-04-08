from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Server(db.model):

    __tablename__ = 'redis_server'

    id = db.Co
