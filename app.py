from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

lr = joblib.load(open("models/model.pkl", 'rb'))

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index1.html")

@app.route("/predict", methods=["POST"])
def predict():
    print('hello')
    sex = int(request.form.get('sex'))
    age = int(request.form.get('age'))
    cp = int(request.form.get('cp'))
    trestbps = int(request.form.get('trestbps'))
    chol = int(request.form.get('chol'))
    fbs = int(request.form.get('fbs'))
    restecg = int(request.form.get('restecg'))
    thalach = int(request.form.get('thalach'))
    exang = int(request.form.get('exang'))
    oldpeak = float(request.form.get('oldpeak'))
    slope = int(request.form.get('slope'))
    ca = int(request.form.get('ca'))
    thal = int(request.form.get('thal'))

    input_data = [[sex, age,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
    pred = lr.predict(input_data)
    pred = 1 if pred == 1 else 0
    print('world')

    return render_template("index1.html", prediction=pred, parameter=input_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)