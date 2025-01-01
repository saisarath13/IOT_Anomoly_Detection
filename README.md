# Anomaly Detection

## Overview
**Anomaly Detection** is a Flask-based web application designed to identify anomalies in temperature data using a trained TensorFlow autoencoder model. The application integrates MQTT for real-time data simulation and is deployed on **Google Cloud Platform (GCP)** for scalable cloud-based execution.

---

## Features
- **Real-time Monitoring**: Captures and plots temperature data in real-time via MQTT.
- **Anomaly Detection**: Uses an autoencoder to detect anomalies in temperature readings.
- **Interactive Web Interface**: Users can input temperature data and receive anomaly detection results.
- **Dockerized Deployment**: Easy setup and deployment using Docker.
- **Cloud Deployment**: Hosted on GCP for high availability and scalability.

---

## Installation

### Prerequisites
- Python 3.12+
- Docker (optional, for containerized deployment)
- GCP account (for deployment)

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/anomaly-detection.git
   cd anomaly-detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Access the application at `http://127.0.0.1:8080`.

---

## Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t anomaly-detection .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8080:8080 anomaly-detection
   ```

3. Access the application at `http://localhost:8080`.

---

## Deployment on GCP

1. Create a GCP project and enable Cloud Run.
2. Build and push the Docker image to Google Container Registry (GCR):
   ```bash
   gcloud builds submit --tag gcr.io/your-project-id/anomaly-detection
   ```
3. Deploy the image to Cloud Run:
   ```bash
   gcloud run deploy anomaly-detection --image gcr.io/your-project-id/anomaly-detection --platform managed
   ```
4. Access the deployed service using the URL provided by GCP.

---

## MQTT Real-Time Data Simulation

1. Simulate temperature data:
   ```bash
   python simulate_temperature_data.py
   ```
   - Simulates temperature readings and publishes them to the MQTT topic `iot/temperature`.

2. Real-time monitoring:
   - The application listens to the MQTT broker and updates a live plot with temperature data.

---

## Project Structure
```
anomaly-detection/
├── app.py                # Main Flask application
├── simulate_temperature_data.py  # MQTT data simulator
├── requirements.txt      # Dependencies
├── Dockerfile            # Docker configuration
├── templates/
│   └── index.html        # Web interface template
├── scaler.pkl            # Pre-trained scaler
├── temperature_anomaly_model.keras  # Trained TensorFlow model
└── README.md             # Project documentation
```

---

## API Endpoints
### **`/`** (GET/POST)
- **Description**: Web interface for anomaly detection.
- **POST Request**:
  - Accepts temperature data from the user.
  - Returns the detection result (`normal` or `anomaly`) and reconstruction error.

---

## Technologies Used
- **Flask**: Web framework for serving the application.
- **TensorFlow**: Used for building and training the autoencoder model.
- **MQTT**: Real-time data simulation and communication.
- **Docker**: Containerization for deployment.
- **GCP Cloud Run**: Scalable cloud hosting.

---

## Future Enhancements
- **Integration with IoT devices**: Extend support for hardware-based temperature sensors.
- **Improved anomaly visualization**: Add advanced graphs and dashboards.
- **Enhanced scalability**: Implement horizontal scaling for high-frequency data streams.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For inquiries or contributions, please reach out to:
- **Email**: sarathk1307@gmail.com
- **GitHub**: [Your GitHub Profile](https://github.com/your-profile)


