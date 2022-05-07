from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mastermindweb.game.gaming import generatenumbercombination, initializesession, resetdata, calculateposition, gethints
from mastermindweb.game.gaming import generatenumbercombination, gamesettings
from mastermindweb.game.forms import GuessingForm
from flask_restful import abort
from mastermindweb import db
from mastermindweb import app
from flask import Flask, session


game = Blueprint('game', __name__)


# Page for User to choose level
@game.route('/dificulty', methods=['GET', 'POST'])
def chooselevel():
    return render_template('game_pages/levelpage.html')


# View page that runs the game
# Game difficulty is chosen based on passed parameter
@game.route('/startgame/<level>/mastermind', methods=['GET', 'POST'])
def startgame(level):
    # Initialize session dictionnary in order to store values based on cookies
    initializesession()
    is_valid, LIMIT = False, True
    hints, maxattempts = [], 10
   
    form = GuessingForm()  # User input form

    current_level = level 

    ############################## If user restarts page ############################################
    if request.method == 'POST':
        post_restart = request.form.get('restart')
        if post_restart is not None:
            resetdata()
            generatenumbercombination(gamesettings[current_level].length, gamesettings[current_level].number_diff - 1)
            return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,maxattempts-session['attempts']), 
                            correctposition=0, wrongposition=0, digitlen=len(session['answer']), maxnum=gamesettings[current_level].number_diff - 1,hints=hints)





    user_guess = form.guesscombo.data #Retrieve user input from Flask Forms
    is_valid = True if form.validate_guess(user_guess, current_level) and user_guess != 'None' else False #is_valid boolean for string processing, changes criteria based on level parameter


    ############################ If Input passed by User is not valid #####################################
    if not is_valid and session['startedgame']: #Also checking for if game started as blank form when you first clicked on page is False per our above processing
        print("There is error in passed in guess")
        flash('Please enter a valid number combination!') 
        return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,maxattempts-session['attempts']), 
                            correctposition=0, wrongposition=0, digitlen=len(session['answer']), maxnum=gamesettings[current_level].number_diff - 1, hints=hints)
    

    if session['startedgame'] == True:
        hints = gethints()
        print(hints)

    positions = calculateposition(user_guess) # Process which user input for correctness  ----> reds : whites
    correctposition, wrongposition = positions.REDS, positions.WHITES


    if is_valid: session['guesses'].append((user_guess, correctposition, wrongposition)) # Save down previous valid user inputs for Hints
    
    
    print(f"Previous guesses are {session['guesses']}")
    print((user_guess, session['answer'] if session['answer'] else ""))






    ############################# Notifiy User if they find correct answer and reinitilize/reset game state ##########################
    if is_valid and user_guess == session['answer']: 
        print(f"You have found the correct positions in {session['attempts']} attempt(s)")
        attempts = session['attempts']
        resetdata(restart=True)
        positions = (0, 0)
        flash('Congratulations, You have won the game in {} attempts(s)'.format(attempts + 1))
        return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,maxattempts - attempts), 
                            correctposition=correctposition, wrongposition=wrongposition, digitlen=len(session['answer']), maxnum=gamesettings[current_level].number_diff - 1)
    
    ############################ If User exhausts Maximum attempts count #####################################
    elif LIMIT and maxattempts - session['attempts'] == 1 and user_guess != session['answer']: #Also checking for if LIMIT mode is activated as well if User has raminingattempts
        flash('No more attempts left. Please restart game and try again!!!!') 
        return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,maxattempts-session['attempts']), 
                            correctposition=0, wrongposition=0, digitlen=len(session['answer']), maxnum=gamesettings[current_level].number_diff - 1, hints=hints)

    
    print(f"Session attempts: {session['attempts']}        Has game started ? : {session['startedgame']}")










    ###########################Generate a new combination only when a new game (attempts==0) ##############################
    if session['attempts'] == 0 and not session['startedgame'] and not session['answer']:
        generatenumbercombination(gamesettings[current_level].length, gamesettings[current_level].number_diff - 1)

    

    session['attempts'] += 1 if is_valid else 0 # Only count valid attempts 
    session['startedgame'] = True # Change state of game to 'started'
    print(f"guess: {user_guess}  attempts: {session['attempts']}")

    ##########################If we arrive here, we have not yet found the answer however our User input was valid ####################
    return render_template('game_pages/gamepage.html', form=form, answer=session['answer'], attempts=max(0,maxattempts-session['attempts']), 
                            correctposition=correctposition, wrongposition=wrongposition, digitlen=len(session['answer']), maxnum=gamesettings[current_level].number_diff - 1,hints=hints)





    









