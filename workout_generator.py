import random

def define_reps(goal):
    if goal == "forca":
        return "3-5 reps"
    elif goal == "hipertrofia":
        return "6-12 reps"
    elif goal == "resistencia":
        return "12-20 reps"
    else:
        return "8-12 reps"

def define_rest(goal):
    if goal == "forca":
        return "90-120s"
    elif goal == "hipertrofia":
        return "60-90s"
    else:
        return "30-60s"

def filter_exercises(exercises, user):
    return [
        e for e in exercises
        if e["level"] in [user["level"], "iniciante"]  # permite regressões
        and (e["equipment"] in user["equipment"] or e["equipment"] == "nenhum")
    ]

def split_workout(days):
    if days == 3:
        return ["push", "pull", "legs"]
    elif days == 4:
        return ["push", "pull", "legs", "core"]
    else:
        return ["full"]

def generate_workout(user, exercises):
    filtered = filter_exercises(exercises, user)
    split = split_workout(user["days_per_week"])

    weekly_plan = []

    for day_type in split:
        if day_type == "full":
            day_exercises = random.sample(filtered, min(5, len(filtered)))
        else:
            day_exercises = [e for e in filtered if e["group"] == day_type]
            day_exercises = random.sample(day_exercises, min(4, len(day_exercises)))

        workout_day = []
        for ex in day_exercises:
            workout_day.append({
                "exercise": ex["name"],
                "sets": 3,
                "reps": define_reps(user["goal"]),
                "rest": define_rest(user["goal"])
            })

        weekly_plan.append({
            "day_type": day_type,
            "workout": workout_day
        })

    return weekly_plan