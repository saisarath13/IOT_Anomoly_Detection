from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib
import os

app = Flask(__name__)

# Load the trained model
model = load_model('temperature_anomaly_model.keras')

# Load the scaler used during training
scaler = joblib.load('scaler.pkl')

# Define the anomaly detection threshold
THRESHOLD = 0.5

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        # Get the temperature data from the form
        temperature = request.form.get('temperature')

        if not temperature:
            error = "No temperature data provided"
        else:
            try:
                # Convert temperature to float
                temperature = float(temperature)

                # Normalize the temperature data
                normalized_data = scaler.transform([[temperature]])
                
                # Get model reconstruction and calculate error
                reconstructed_data = model.predict(normalized_data)
                reconstruction_error = np.mean(np.square(normalized_data - reconstructed_data))
                
                # Determine status
                status = "anomaly" if reconstruction_error > THRESHOLD else "normal"
                
                # Prepare the result
                result = {
                    "status": status,
                    "temperature": temperature,
                    "error": reconstruction_error
                }
            except Exception as e:
                error = str(e)

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
