from sklearn.metrics import mean_absolute_error
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
xgb = pickle.load(open("models/xgb_model.pkl", 'rb'))

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    print('Hello world')

    minimum_nights = float(request.form['minimum_nights'])
    room_type = int(request.form['room_type'])
    number_of_reviews = float(request.form['number_of_reviews'])
    reviews_per_month = float(request.form['reviews_per_month'])
    calculated_host_listings_count = float(request.form['calculated_host_listings_count'])
    neighbourhood_group = int(request.form['neighbourhood_group'])
    availability_365 = int(request.form['availability_365'])
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])

    input_data = [[minimum_nights, number_of_reviews, calculated_host_listings_count, neighbourhood_group, room_type, reviews_per_month, availability_365, latitude, longitude]]
    predicted_price = xgb.predict(input_data)

    print('Hello worl2222d')

    # mae = mean_absolute_error(actual_price, predicted_price)
    # print(f'Mean Absolute Error (MAE): {mae:.2f}')

    return render_template("index.html", prediction=predicted_price, parameter=input_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

