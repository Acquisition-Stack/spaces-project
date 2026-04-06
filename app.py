from flask import Flask, render_template
import random
import time

app = Flask(__name__)

#Generate a random number for listeners:
# Module-level state (lives as long as the server runs)
active_listeners = random.randint(1, 12)
last_updated = time.time()
UPDATE_INTERVAL = 5000 # seconds

@app.route("/")
def coffee_spaces():

    global active_listeners, last_updated

    if time.time() - last_updated >= UPDATE_INTERVAL:
        active_listeners = random.randint(1, 10)
        last_updated = time.time()

    return render_template("/index.html", active_listeners=active_listeners)



        # REFACTOR
    # You should make the amount of rooms dynamic later on. 
    # Setup a struct and have the rooms appear dynamically.

@app.route("/space")
def tokyo_night():
    return render_template("/space.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

