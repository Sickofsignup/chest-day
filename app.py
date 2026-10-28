
from flask import Flask, render_template, request

app = Flask(__name__)


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

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
