from random import randint
from flask import Flask, render_template, session, request, redirect # Import Flask to allow us to create our app 
import random 

app = Flask(__name__) # Create a new instance of the Flask class called "app" 
app.secret_key = 'magic number game'

@app.route('/')
def homepage():
    if 'numberActual' not in session:
        session['numberActual'] = random.randint(1, 100)
    
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['numberGuess'] = int(request.form['numberGuess'])
    return redirect('/')

@app.route('/reset')
def resetgame():
    session.clear()
    return redirect('/')

if __name__=="__main__": # Ensure this file is being run directly and not from a different module  
    app.run(debug=True, port=5001) # Run the app in debug mode. 