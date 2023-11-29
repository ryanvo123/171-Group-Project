from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    # Extract input values from the form
    user_id = int(request.form.get('userId'))
    movie_id = int(request.form.get('movieId'))

    # Pass the inputs to the model
    prediction = model.predict(user_id, movie_id)

    # Assuming your model output is a single value
    result = prediction[3]

    return render_template("index.html", prediction="Estimated movie rating is {}".format(result))

if __name__ == '__main__':
    app.run(debug=True)

