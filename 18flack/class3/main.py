from flask import Flask ,render_template

## initilize flask

app = Flask(__name__)

## make a home page

@app.route('/')
def welcame():
    return "welcame to my home  page"
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

## entry point

if __name__ == "__main__":
    app.run(debug=True)
    
