from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def create_db():
    conn = sqlite3.connect("workout_db.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS exercise_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    exercise TEXT NOT NULL,
                    weight FLOAT,
                    reps INTEGER,
                    date DATE NOT NULL
                )''')
    conn.commit()
    conn.close()

# Route to render the index.html page
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/track")
def track_workout():
    return render_template("track.html")

@app.route("/progress")
def view_progress():
    return render_template("progress.html")

if __name__ == "__main__":
    create_db()
    app.run(debug=True)
