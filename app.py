from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def coffee_spaces():
    return render_template("/index.html")

        # REFACTOR
    # You should make the amount of rooms dynamic later on. 
    # Setup a struct and have the rooms appear dynamically.

@app.route("/space")
def tokyo_night():
    return render_template("/space.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

