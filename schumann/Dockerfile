# Use the official lightweight Python image.
FROM python:3.8-slim

# Set the working directory to /app.
WORKDIR /app

# Install Flask and any other dependencies
RUN pip install flask

# Make port 5000 available to the world outside this container.
EXPOSE 5000

# Define environment variable.
ENV FLASK_APP=app.py

# The command is now provided by docker-compose.yml