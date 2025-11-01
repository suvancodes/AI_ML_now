from flask import Flask

## initilize flask

app = Flask(__name__)

## make a home page

@app.route('/')
def welcame():
    return "welcame dks to my home  page"
@app.route('/index')
def index():
    return "welcame dks to my index  page"

## entry point

if __name__ == "__main__":
    app.run(debug=True)
    
