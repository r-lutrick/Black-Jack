from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
# Import other MODEL FILEs to prevent circular import
# from flask_app.models import flask_app_model


class Game:
    def __init__(self, data):
        self.id = data["id"],
        self.dealer = data["dealer"]
        self.player = data["player"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
