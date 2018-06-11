from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = "#$4f24f0s9as8d752f#$^@1ds-11t3qdsaC"
@app.route('/')
def table():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():
    
    if 'Reset' in request.form:
        if request.form['Reset'] == 'Reset':
            session.clear()
            return redirect('/')
        
    print(request.form)

    allfieldsValid = True

    if len(request.form['name']) < 1:
        flash("A name is required!")
        allfieldsValid = False
    if len(request.form['comment']) < 1:
        flash("You must provide a comment!")
        allfieldsValid = False
    elif len(request.form['comment']) > 120:
        flash("Your comment must be less than 120 characters")
        allfieldsValid = False
    
    if allfieldsValid:
        session.clear()
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return render_template('index2.html')
    else:
        return redirect('/')



@app.route('/danger', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":

    app.run(debug=True)