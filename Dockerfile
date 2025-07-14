# Base image
FROM python:3.11-slim-bullseye

# Working directory
WORKDIR /app

# Prevent .pyc files, force stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Copy app code
COPY . .

# Install dependencies
RUN pip install flask

# Expose port for Cloud Run
EXPOSE 8080

# Run the Flask app
CMD ["python", "application.py"]
