import  flask
from flask import Flask, render_template, request , url_for 

from datetime import datetime
app = Flask(__name__)

# Home page get the courses name 
# get courses name function from courses.txt

def get_courses():
    coursesdb = open("courses.txt")
    content = coursesdb.read()
    coursesdb.close()
    courses = content.split("\n")
    return courses

# route to courses page and retrive the courses name

@app.route("/courses")
def course():
    html_file = open("templates/courses.html")
    content = html_file.read()
    html_file.close()
    courses = get_courses()
    actual_values = ""
    for course in courses:
        actual_values+="<p>"+ course + "</p>"
    return content.replace("$$COURSES$$", actual_values)


# create a search for courses page
@app.route("/search")
def search():
    html_file = open("templates/courses.html")
    content = html_file.read()
    html_file.close()
    query = flask.request.args.get("q")
    courses = get_courses()
    result = ""
    for course in courses:
        if course.lower().find(query.lower()) != -1:
            result+= "<p>"+ course + "</p>"
    if result =="":
        result= "<p> No result found </p>"
   
    return content.replace("$$COURSES$$", result)
    



# calculate user years old
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def calculate_age(self):
        current_year = datetime.now().year
        age = current_year - self.birth_year
        return age




# route the home page
@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def home():
    if request.method == "POST":
        name = request.form["name"]
        birth_year = int(request.form["birth_year"])
        person = Person(name, birth_year)
        age = person.calculate_age()
        return render_template("result.html", name=name, age=age)
    return render_template('index.html')



@app.route("/python")
def python():
    return render_template('python.html')

@app.route("/javaScript")
def java_script():
    return render_template('javaScript.html')


if __name__ == '__main__':
    app.run(debug=True)