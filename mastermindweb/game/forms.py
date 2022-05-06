# Form Based Imports
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired,Email,EqualTo, NumberRange
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask import request
from mastermindweb.game.gaming import gamesettings

# User Based Imports
from flask_login import current_user
from mastermindweb.models import User


class GuessingForm(FlaskForm):
    guesscombo = StringField('guess',validators=[DataRequired()])
    submit = SubmitField('Guess!')

    def validate_guess(form, field, curr_level):
        if not field or len(str(field)) != gamesettings[curr_level].length: return False
        
        guess = str(field)
        for c in guess:
            if not c.isdigit() or int(c) > gamesettings[curr_level].number_diff - 1: #8 different digits, 7 is top
                return False
        return True

