from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/track', methods=['GET', 'POST'])
def track_workout():
    if request.method == "POST":
        chosen_workout = request.form.get("workouts")

        workout_dict = {
            "Shoulders and Triceps": {
                "Shoulder Press": 4,
                "Lateral Raises": 4,
                "Rear Delt Fly": 3,
                "Tricep Pushdown": 4,
                "Tricep Extensions": 4,
            },
            "Back": {
                "Pull Ups": 3,
                "Close Grip Rows": 4,
                "Pulldowns": 3,
                "Single Arm Machine Row": 3,
            },
            "Chest and Biceps": {
                "Flat Bench Press": 3,
                "Incline Bench Press": 3,
                "Pec Fly": 3,
                "Hammer Curls": 3,
                "Barbell Curls": 3,
            },
            "Legs and Abs": {
                "Leg Extensions": 2,
                "Squats": 4,
                "Deadlifts": 3,
                "Machine Crunches": 3,
                "Plank": 2,
            }
        }

        exercise_details = workout_dict.get(chosen_workout, {})

        return render_template("track.html", chosen_workout=chosen_workout, exercise_details=exercise_details)
    else:
        default_value = "None"
        return render_template("track.html", chosen_workout=default_value, exercise_details={})



@app.route("/progress")
def view_progress():
    return render_template("progress.html")

def workout_details(workout):
    exercise_details = {}

    if workout == "Shoulders and Triceps":
        exercises = ["Shoulder Press", "Lateral Raises", "Rear Delt Fly", "Tricep Pushdown", "Tricep Extensions"]
        sets = [4, 4, 3, 4, 4]
    elif workout == "Back":
        exercises = ["Pull Ups", "Close Grip Rows", "Pulldowns", "Single Arm Machine Row"]
        sets = [3, 4, 3, 3]
    elif workout == "Chest and Biceps":
        exercises = ["Flat Bench Press", "Incline Bench Press", "Pec Fly", "Hammer Curls", "Barbell Curls"]
        sets = [3, 3, 3, 3, 3]
    elif workout == "Legs and Abs":
        exercises = ["Leg Extensions", "Squats", "Deadlifts", "Machine Crunches", "Plank"]
        sets = [2, 4, 3, 3, 2]
    else:
        # Default if workout is not recognized
        exercises = []
        sets = []

    # Construct the exercise_details dictionary
    for i in range(len(exercises)):
        exercise_details[exercises[i]] = sets[i]

    return exercise_details


if __name__ == "__main__":
    create_db()
    app.run(debug=True)
