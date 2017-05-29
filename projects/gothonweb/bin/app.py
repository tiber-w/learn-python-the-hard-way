from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='../templates')

@app.route('/')
def index():
    greeting = 'Hello, World!'
    return render_template("index.html", greeting=greeting)

#@app.route('/1')
#def page1():
#    return render_template("index.html", greeting='This is page 1!')

if __name__ == "__main__":
    #app.debug = True
    app.run()
