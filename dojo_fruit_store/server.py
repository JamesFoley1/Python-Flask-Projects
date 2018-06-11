from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    date= datetime.datetime.now()
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    blackberry = request.form['blackberry']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    total = int(strawberry) + int(raspberry) + int(apple) + int(blackberry)
    return render_template("checkout.html", strawberry = strawberry, raspberry = raspberry, apple = apple, blackberry = blackberry,
    first_name = first_name, last_name = last_name, student_id = student_id, total = total, date = date)

@app.route('/fruits')         
def fruits():

    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    