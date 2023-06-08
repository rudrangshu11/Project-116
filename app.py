# importing modules from flask library
from flask import Flask, render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Rudrangshu Sengupta" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father_webpage():

    father_name = "Dwaipayan Sengupta"
    father_age="43"

    return render_template("father.html", name= father_name, age=father_age)

# define the route to mother webpage
@app.route("/mother")
def mother_webpage():

    mother_name = "Rakhi Sengupta"
    mother_age = "43"

    return render_template("mother.html", name=mother_name, age=mother_age)

# define the route to friends webpage
@app.route("/friend")
def friend_webpage():

    friend_name = "Rishita Dhali"
    friend_age = "15"

    return render_template("friend.html", name=friend_name, age=friend_age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
