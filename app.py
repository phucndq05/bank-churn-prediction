from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd

# Initialize the app
app = Flask(__name__)

# Load the trained model and scaler from the 'deployment' folder
model = joblib.load('deployment/model.pkl')
scaler = joblib.load('deployment/scaler.pkl')

# Define the feature order required by the model
# THIS ORDER MUST BE EXACTLY THE SAME AS WHEN THE MODEL WAS TRAINED
feature_order = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 
                 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 
                 'Geography_Germany', 'Geography_Spain', 'Gender_Male']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Create a dictionary for all expected features with a default of 0
    form_features = {feature: 0 for feature in feature_order}

    # Get the input data from the form
    form_data = request.form.to_dict()
    
    # Update the dictionary with numerical values from the form
    for key, value in form_data.items():
        if key in feature_order:
            form_features[key] = float(value)

    # Handle one-hot encoded features based on form selection
    if form_data.get('Geography') == 'Germany':
        form_features['Geography_Germany'] = 1
    if form_data.get('Geography') == 'Spain':
        form_features['Geography_Spain'] = 1
    if form_data.get('Gender') == 'Male':
        form_features['Gender_Male'] = 1

    # Create a DataFrame in the correct order
    input_df = pd.DataFrame([form_features])
    
    # Scale the input data using the loaded scaler
    scaled_input = scaler.transform(input_df)
    
    # Make a prediction
    prediction = model.predict(scaled_input)[0]
    
    # Define the output message
    if prediction == 1:
        prediction_text = 'Customer is LIKELY to Churn'
    else:
        prediction_text = 'Customer is LIKELY to Stay'
        
    return render_template('result.html', prediction_text=prediction_text, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)