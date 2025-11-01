from flask import Flask,render_template,request,redirect,url_for

## initilize flask

app = Flask(__name__)

## make a home page

@app.route('/' , methods=['GET'])
def welcame():
    return "welcame dks to my home  page"

@app.route('/index')
def index():
    return "welcame dks to my index  page"

## post request
@app.route('/from',methods = ['GET','POST'])
def form():
    return render_template('from.html')

@app.route('/submit',methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['username']
        return f'hello {name}'
    return render_template('from.html')

## variable rule
## jinja2 -> it had multiple way to read the data form backend and display it in backend


'''
1. {{ }} expression print in a html page
2. {%....%} condition and for loop
3. {#....#} this is for comments
'''

# mathod 1

@app.route('/mark/<int:score>')
def mark(score):
    if(score>50):
        res = 'PASS'
    else:
        res = 'FAIL'
    return render_template('result.html',result = res)

# mathod 2

## for loop

@app.route('/mark1/<int:score>')
def mark1(score):
    if(score>50):
        res = 'PASS'
    else:
        res = 'FAIL'
        
    exp = {'mark' : score ,'result' : res}
    return render_template('for.html',result = exp)

# for if else 

@app.route('/markif/<int:score>')
def markif(score):
    return render_template('if.html',result = score)


# redirect  -> used to redirect to any redirect to any url 
# url_for-> used to make dynamisc url 

@app.route('/form', methods=['GET', 'POST'])
def get_res():
    total = 0
    if request.method == 'POST':
        math = float(request.form['math'])
        phy = float(request.form['phy'])
        che = float(request.form['che'])
        total = math+che+phy 
        return redirect(url_for('markif', score=total))
    else:
        return render_template('form.html')



## entry point

if __name__ == "__main__":
    app.run(debug=True)
    
