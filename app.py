from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('adam_nn.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [
        int(data['friends']),
        1 if data['leadership'] == 'Yes' else 0,
        data['hobbies'],
        data['inasis']
    ]
    
    # Transform categorical variables if necessary
    hobbies_mapping = {
        'physical': 1, 
        'creative': 5, 
        'cerebral': 2, 
        'making-tinkering': 4, 
        'community-activities': 3, 
        'collecting': 6
    }
    inasis_mapping = {
        'MAYBANK': 1, 
        'PROTON': 1, 
        'TRADEWINDS': 1, 
        'MAS': 1, 
        'TNB': 1, 
        'YAB': 3, 
        'MUAMALAT': 3, 
        'BSN': 2, 
        'TM': 2, 
        'BANK ISLAM': 2, 
        'SIME DARBY': 2, 
        'PETRONAS': 3, 
        'SME': 4, 
        'PERSISIRAN SINTOK': 5, 
        'TAMAN UNI': 5
    }

    features[2] = hobbies_mapping[features[2]]
    features[3] = inasis_mapping[features[3]]
    
    prediction = model.predict([features])
    
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
