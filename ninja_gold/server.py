from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)
app.secret_key = "#41Ui10033004@#$%055#!#$31Fff1"

def makesession():
    if 'ninja' not in session:
        session['ninja'] = ''
        session['total'] = 0
        session['building'] = 0
        session['activity'] = ""
        session['num'] = 0
        session['p'] = []
        session['date'] = datetime.datetime.now()
    print(session)
@app.route('/')
def index():
    makesession()
    return render_template('index.html')

@app.route('/process_money', methods=['Post'])
def process():
    makesession()
    session['building'] = request.form['building']
    
    if session['building'] == "farm":
        session['num'] = random.randrange(10, 21)
        session['total'] += session['num']
        session['activity'] = "<p style='color: green;'>" + "Earned " + str(session['num']) + " gold from the " + str(session['building']) + "! " + str(session['date']) + "</p>"
        session['p'].insert(0, session['activity'])

    elif session['building'] == "cave":
        session['num'] = random.randrange(10, 21)
        session['total'] += session['num']
        session['activity'] = "<p style='color: green;'>" + "Earned " + str(session['num']) + " gold from the " + str(session['building']) + "!</p>"
        session['p'].insert(0, session['activity'])

    elif session['building'] == "house":
        session['num'] = random.randrange(2, 6)
        session['total'] += session['num']
        session['activity'] = "<p style='color: green;'>" + "Earned " + str(session['num']) + " gold from the " + str(session['building']) + "!</p>"
        session['p'].insert(0, session['activity'])

    elif session['building'] == "casino":
        session['num'] = random.randrange(-50, 51)
        session['total'] += session['num']
        if session['num'] > -1:
            session['activity'] = "<p style='color: green;'>" + "Earned " + str(session['num']) + " gold from the " + str(session['building']) + "!</p>"
            session['p'].insert(0, session['activity'])

        elif session['num'] < 0:
            session['activity'] = "<p style='color: red;'>" + "Earned " + str(session['num']) + " gold from the " + str(session['building']) + "!</p>"
            session['p'].insert(0, session['activity'])
    

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":

    app.run(debug=True)