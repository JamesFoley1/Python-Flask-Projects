from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def table():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    return render_template('index2.html', name = name, location = location, language = language, comment = comment)

@app.route('/danger', methods=['POST'])
def reset():
    print("a user tried to visit /danger")
    return redirect('/')

if __name__=="__main__":

    app.run(debug=True)