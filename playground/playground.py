from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Welcome To My World!"

@app.route('/play/<num>')
def makeBox(num):
    return render_template('index.html', newNum = int(num), 
    head = "Welcome!")

@app.route('/play/<num>/<color>')
def makeBoxes(num, color):
    return render_template('index.html', newNum = int(num), 
    head = "Welcome!", newColor = color )


app.run(debug=True)