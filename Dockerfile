# Dockerfile for Flask application with TensorFlow

# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Run the application
CMD ["python", "app.py"]
