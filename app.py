from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    foods = ["Hamburger", "Sushi", "Ice-Cream"]
    animals = ["Dog", "Cat", "Lion"]
    return render_template("index.html", foods=foods, animals=animals,
    opposite_day = False)

if __name__ == '__main__':
   app.run(debug = True)
