import json
import requests
import os
from mastermindweb import app
from flask import Flask, session
from flask_session import Session
from flask import render_template, url_for, flash, redirect, request, Blueprint
from collections import namedtuple, Counter

os.geten
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


# combination_len --> represents how many digits combination can contain
# numberof_combination --> represesents the total different numbers combination can have
def generatenumbercombination(combination_len, numberof_combination):
    url = 'https://api.random.org/json-rpc/1/invoke'    # API enpoint

    # Retrieve hidden API_KEY from Heroku environment
    random_org_api_key = os.getenv('API_KEY', 'None')
    
    #Query Parameters to filter returned data
    data = {'jsonrpc':'2.0','method':'generateIntegers','params': {'apiKey':random_org_api_key,'n':combination_len,'min':0,'max':numberof_combination - 1,'replacement':'true','base':10},'id':24565}

    params = json.dumps(data) #Convert dict to json format
    response = requests.get(url,params) # Inititate " GET " request


    try:
        response = requests.post(url,params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh: # raised if there is a 404 error
        print(errh)
    except requests.exceptions.ConnectionError as errc: # raised if no response from server
        print(errc)
    except requests.exceptions.Timeout as errt: # raised if request doesn't complete within alloted time
        print(errt)
    except requests.exceptions.RequestException as err: #raised if hhtp error 
        print(err)

    
    jsondict = Counter(response.json()) #Obtain response in json/dictionnary format
    data = jsondict['result']['random']['data'] # get value in key data
    code_combination = ''.join(map(str,data)) if isinstance(data, list) else '' # Convert List[int] -> string 


    #Add response/answer to session
    session["answer"] = code_combination


# Format: List:tuple:[(user_guess, correctpos, wrongpos)]
def gethints():
    return session['guesses']
                

