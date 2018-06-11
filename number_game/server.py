from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "Keep it secret keep it safe"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
    session['guess'] = request.form['guess']
    session['correct'] = ""
    guess = ""
    
    if 'comp' not in session:
        session['comp'] = random.randrange(0,101)

    if session['guess'] != "":
        guess = int(session['guess'])
        if guess == session['comp']:
            session['correct'] = "You are correct!"
        elif guess < session['comp']:
            session['correct'] = "Too Low!"
        elif guess > session['comp']:
            session['correct'] = "Too High!"

    print(session['comp'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":

    app.run(debug=True)