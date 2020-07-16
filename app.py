from flask import Flask,render_template,request, redirect, url_for, flash
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/article"

mongo = PyMongo(app)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/signup',methods = ['POST','GET'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        mongo.db.users.insert_one(
            {
                'fname': first_name,
                'lname': last_name,
                'email': email,
                'password': password
            }
        )
        flash("Account created successfully","success")
        
    return render_template("signup.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")




if __name__ == '__main__':
    app.secret_key = "sdfbh"
    app.run(debug=True)