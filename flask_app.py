from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("modele.pkl", "rb"))


def model_pred(features):
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])


@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        Age = int(request.form["Age"])
        InterestRate = int(request.form["InterestRate"])
        LoanTerm = int(request.form["LoanTerm"])
        MonthsEmployed = float(request.form["MonthsEmployed"])
        Income = int(request.form["Income"])

        prediction = model.predict(
            [[Age, InterestRate, LoanTerm, MonthsEmployed, Income]]
        )

        if prediction[0] == 1:
            return render_template(
                "index.html",
                prediction_text="Default = 1",
            )

        else:
            return render_template(
                "index.html", prediction_text="Default = 0"
            )

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
