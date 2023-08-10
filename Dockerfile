# Use the official Python image as base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

RUN apt-get update && apt-get install -y curl

# Install the Flask library
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY configmap_app.py .

# Expose the port the app runs on
EXPOSE 80

# Set environment variables. Create this variables in your application.
ENV PROD_ENV "NetworkingAPP_PROD"
ENV DNS_IP "Unknown"

# Command to run the application
CMD ["python", "configmap_app.py"]

