
from flask import Flask, render_template, request
import random

app = Flask(__name__)

GYM_EXCUSES = [
    "My pre-workout hasn't emotionally prepared me 💀",
    "The bench looked at me funny 😭",
    "Mercury is in retrograde and my pecs sensed danger 🪐",
    "My gym fit is in the washing machine. Can't train like this.",
    "I sneezed this morning. Chest day is too risky 🤧",
    "My muscles are updating. Please wait... 99% 💀",
    "I couldn't find my headphones. Workout cancelled 🎧",
    "The gym playlist was NOT giving today 😭",
    "I had to let my protein digest for 6-8 business days 🍗",
    "My left pec said yes but my right pec said no 💀",
    "I was gonna go, but my bed hit a PR in keeping me asleep 🛌",
    "My creatine hasn't finished loading yet ⚡",
    "The bench press machine is probably busy. Better not risk it.",
    "I'm saving my strength for the zombie apocalypse 🧟",
    "My ancestors told me to rest today. Who am I to argue? 🗿",
]

LEG_VERDICTS = [
    "BRO TRAINED LEGS BEFORE CHEST 😭 THIS IS A CHEST DAY WEBSITE.",
    "Quads built like a Greek god, pecs built like a missing person 💀",
    "Leg day is NOT a legal defence. GUILTY. ⚖️",
    "BRO GOT TREE TRUNKS FOR LEGS AND PANCAKES FOR PECS 😭",
    "The legs are thriving. The chest is filing a missing persons report.",
    "SQUATS?! IN THIS ECONOMY?! YOUR PECs ARE STILL WAITING 💀",
    "Your thighs got promoted. Your chest got laid off 😭",
    "GYM COURT SENTENCES YOU TO ONE CHEST SESSION. NO APPEALS. ⚖️",
]


def get_message(answer, pr=None):
    if answer == "yes":
        if pr is None:
            return "Enter your bench PR first!"

        if pr < 60:
            return "your a bum 💀"
        elif pr == 60:
            return "one plate, niceee"
        elif pr < 95:
            return "wow more than one plate well done"
        elif pr <= 99:
            return "Bro your so close to 100 😭"
        elif pr == 100:
            return "WOW 100???!!! 🔥"
        elif pr <= 199:
            return "over 100kg?!?! wow your pretty strong"
        elif pr <= 299:
            return "OVER 200KG?!?!?! Wow your really really strong"
        else:
            return "its either lies or roids 💀"

    elif answer == "no":
        return "go hit chest then 💀"

    elif answer == "idk":
        return "well go hit it just incase"

    elif answer == "excuse":
        return random.choice(GYM_EXCUSES)

    elif answer == "legs":
        return random.choice(LEG_VERDICTS)

    return "i dont understand, answer in yes or no please"


@app.route("/", methods=["GET", "POST"])
def home():
    message = None

    if request.method == "POST":
        answer = request.form.get("answer", "").lower().strip()
        pr = request.form.get("pr", "").strip()

        if answer == "yes":
            try:
                weight = float(pr)

                if weight < 0:
                    raise ValueError

                message = get_message(answer, weight)

            except ValueError:
                message = "Enter a valid bench PR in kg!"

        else:
            message = get_message(answer)

    bench_kg = weight if request.method == "POST" and answer == "yes" and "weight" in locals() else None
    return render_template("index.html", message=message, bench_kg=bench_kg)


if __name__ == "__main__":
    app.run(debug=True)
