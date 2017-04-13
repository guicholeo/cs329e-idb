from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "SCREW THIS CRAP"

@app.route('/books')
def books():
    return "WHY ISNT THIS WORKING"

if __name__ == "__main__":
    app.run()
