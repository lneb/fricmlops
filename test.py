from flask_app import model_pred

new_data = {'Age': 68,
            'InterestRate': 10,
            'LoanTerm': 30,
            'MonthsEmployed': 100,
            'Income': 120000,
            }


def test_predict():
    prediction = model_pred(new_data)
    assert prediction == 1, "incorrect prediction"
