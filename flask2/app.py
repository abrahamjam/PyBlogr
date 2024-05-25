from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=['POST'])
def greeter():
    if request.method == 'POST':
        if 'name_input' in request.form:
            flash("Hi " + request.form['name_input'] + ", great to see you!")
        else:
            flash("Something went wrong. Please try again.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

