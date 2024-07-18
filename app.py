from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        hometown = request.form['hometown']
        gpa = float(request.form['gpa'])
        activities = request.form['activities']
        inasis = request.form['inasis']
        income = float(request.form['income'])
        hobbies = request.form['hobbies']
        friends = int(request.form['friends'])
        leadership = request.form['leadership']

        # Assuming you have a model trained to handle these inputs
        # For example, loading a model using pickle
        model_path = 'model/model.pkl'
        with open(model_path, 'rb') as file:
            model = pickle.load(file)

        # Create a dataframe from the inputs
        input_data = pd.DataFrame([[hometown, gpa, activities, inasis, income, hobbies, friends, leadership]],
                                  columns=['hometown', 'gpa', 'activities', 'inasis', 'income', 'hobbies', 'friends', 'leadership'])

        # Make prediction
        prediction = model.predict(input_data)[0]

        return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(debug=True)

