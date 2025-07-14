# Base image (lightweight Python)
FROM python:3.11-slim-bullseye

# Avoid .pyc files and buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies (add git if MLflow ever returns)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -e .



# Expose port Cloud Run expects
EXPOSE 8080

# Start the Flask app
CMD ["python", "application.py"]
