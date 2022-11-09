from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "<h1> I am in home page </h1>"

@app.route('/about')
def about():
    return "<h1> About Me </h1>"

if __name__ == '__main__':
    app.run(debug=True)
