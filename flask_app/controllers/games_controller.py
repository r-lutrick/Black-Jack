from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.game_model import Game
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt(app)


@app.route('/')
def game():
    return render_template('blackjack.html')
