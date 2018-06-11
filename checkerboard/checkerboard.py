from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def checkbox():
    num = 4
    return render_template('checkerboard.html', num = num)


@app.route('/<x>/<y>')
def checkbox2(x,y):
    num1 = int(x)
    num2 = int(y)
    return render_template('checkerboard2.html', num1 = num1, num2 = num2)




app.run(debug=True)