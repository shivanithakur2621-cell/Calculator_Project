from flask import Flask, render_template, request

app = Flask(__name__)

history = []  # store results

@app.route("/", methods=["GET", "POST"])
def calc():
    result = ""
    if request.method == "POST":
        expression = request.form["expression"]
        try:
            result = str(eval(expression))
            with open("history.txt", "a") as f:
                f.write(expression + " = " + result + "\n")
        except:
            result = "Error"

    # Read history
    history = []
    try:
        with open("history.txt", "r") as f:
            history = f.readlines()
    except:
        pass

    return render_template("index.html", result=result, history=history)


if __name__ == "__main__":
    app.run(debug=True)