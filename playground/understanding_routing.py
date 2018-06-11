from flask import Flask, render_template, request
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    if name == "john" or name == "John":
        return "Hi " + name + "!"
    else:
        return "Hi " + name + "."


@app.route('/repeat/<num>/<name>')
def repeat(num, name):
    newnum = int(num)
    return ("\n" + name) * newnum


if __name__ == "__main__":

    app.run(debug=True)
