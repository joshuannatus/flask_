## Create a simple flask application

from flask import Flask, render_template, request,redirect,url_for

## Create the flask app
app = Flask(__name__)

@app.route("/")
def home():
        return "<h1><p>Hello World</p></h1>"
        
@app.route("/welcome")
def welcome():
        return "Welcome to Flask Tutorial"

@app.route("/index")
def index():
        return render_template("index.html")

@app.route("/calucate/<int:scores>")
def calucate(scores):
        return str(scores)

@app.route('/success/<int:score>') 
def success(score):
    return "the person is passed and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is "+str(score)
    

@app.route("/simple", methods=["POST", "GET"])
def simple():
        if request.method=="GET":
                return render_template("maths.html")
        else:
                Mathematics = float(request.form["Mathematics"])
                English= float(request.form["English"])
                Science= float(request.form["Science"])
                
                average_mark = (Mathematics + English + Science)/3
                result = ""
                if average_mark > 50:
                        result = "success"
                else:
                        result = "fail"
                        
                return redirect(url_for(result, score=average_mark))
                
                
                return render_template("maths.html",results=average_mark)



if __name__=="__main__":
    app.run(debug=True)