import random
from mastermindweb import app
from flask import Flask, session
from flask_session import Session
from flask import render_template, url_for, flash, redirect, request, Blueprint
from collections import namedtuple


gaming = Blueprint('game', __name__)
SESSION_TYPE = 'filesystem'
###Remove if causes bugs
app.config.from_object(__name__)

#To share data between requests, we can store data in a session instead of having to store in a database
#A session makes it possible to remember information from one request to another. The way Flask does this is by using a signed cookie
Session(app)


#Create namedtuple in order to access namedfields
# length --> represents how many digits combination can contain
# numberof_diff --> represesents the total different numbers combination can have
Combination = namedtuple('Combination', ['length', 'number_diff'])


#Create namedtuple in order to access namedfields
# REDS --> represents correct number in correct position
# WHITES --> represesents correct number in wrong position
Position = namedtuple('Position', ['REDS', 'WHITES'])





# sets combination settings and criterias
gamesettings = {'easy': Combination(4, 8), 'medium':Combination(5, 8), 'hard': Combination(8, 10)}


def resetdata(restart=False):
    session['attempts'] = 0
    session['answer']= ""
    session['guesses'] = []
    session['level'] = ''
    if not restart:
        session['startedgame'] = False #Handles behavior for restart

def initializesession():
    if "answer" not in session:
        session["answer"]= ""
    if "attempts" not in session:
        session["attempts"] = 0
    if 'guesses' not in session:
        session['guesses'] = []
    if 'startedgame' not in session:
        session['startedgame'] = False
    if 'level' not in session:
        session['level'] = ''
    

# Find RED and WHITE pins
def calculateposition(user_guess):
    reds, whites = 0, 0
    if not session['answer'] or not user_guess: return Position(0, 0)

    answer, guess = session['answer'], user_guess
    if len(answer) != len(guess): return Position(0, 0)

    for key, digit in enumerate(guess):
        if digit == answer[key]:
            reds += 1
        else:
            for answerDigit in answer:
                if answerDigit == digit:
                    whites += 1
                    break   ###Only counting one number if guess equals 2 numbers in given combination

    return Position(reds, whites) if not None else Position(0,0)


# Combination length --> represents how many digits combination can contain
# numberof_combination --> represesents the total different numbers combination can have
def generatenumbercombination(combination_len, numberof_combination):
    code_combination = ""
    for i in range(combination_len):
        code_combination += str(random.randint(0, numberof_combination-1))
    
    #Add response key to session
    session["answer"] = code_combination


# Get hints in decreasing order of total position found #
# Format: List:tuple:[(user_guess, correctpos, wrongpos)]
def gethints():
    return sorted(session['guesses'], key=lambda x: x[1] + x[2], reverse=True)
                

