# Hotel Reservation Cancellation Prediction - MLOps Project

## Overview
This project implements an end-to-end Machine Learning Operations (MLOps) pipeline for predicting hotel reservation cancellations. It integrates data preprocessing, model training, a Flask-based web application, CI/CD with Jenkins, and deployment using Docker and Google Cloud Run (assumed to be added). The project leverages modern MLOps tools and best practices to ensure scalability, reproducibility, and efficient model deployment.

The dataset used is sourced from a hotel reservation system, and the goal is to predict whether a reservation will be canceled based on various features. The pipeline includes data versioning, experiment tracking, model deployment, and automated workflows.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [MLOps Pipeline](#mlops-pipeline)
- [Model Training](#model-training)
- [Web Application](#web-application)
- [CI/CD Pipeline](#cicd-pipeline)
- [Deployment](#deployment)
- [Monitoring and Logging](#monitoring-and-logging)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Structure
```
MLOPS_PROJECT/
├── data/                          # Dataset and data-related files
│   ├── raw/                       # Raw dataset
│   ├── processed/                 # Processed dataset
├── notebooks/                     # Jupyter notebooks for EDA and prototyping
├── src/                           # Source code for the project
│   ├── data_preprocessing.py      # Data cleaning and preprocessing
│   ├── model_training.py          # Model training and evaluation
│   ├── app.py                    # Flask web application
│   ├── predict.py                # Prediction script
│   ├── utils.py                  # Utility functions
├── tests/                         # Unit and integration tests
├── Dockerfile                    # Docker configuration
├── Jenkinsfile                   # Jenkins CI/CD pipeline configuration
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── .gitignore                    # Git ignore file
├── mlflow/                       # MLflow tracking artifacts
└── scripts/                      # Automation scripts
```

---

## Features
- **End-to-End MLOps Pipeline**: Covers data preprocessing, model training, experiment tracking, deployment, and monitoring.
- **Data Versioning**: Uses DVC for versioning datasets and models to ensure reproducibility.
- **Experiment Tracking**: MLflow for tracking experiments, hyperparameters, and model performance.
- **Flask Web App**: A user-friendly web interface for making predictions.
- **CI/CD Integration**: Automated testing, building, and deployment using Jenkins and GitHub Actions.
- **Containerization**: Docker for packaging the application and dependencies.
- **Cloud Deployment**: Assumed deployment to Google Cloud Run for scalable, serverless hosting.
- **Modular Codebase**: Organized and maintainable code structure for scalability.

---

## Technologies Used
- **Programming Language**: Python 3.8+
- **Machine Learning**: Scikit-learn, XGBoost
- **Data Versioning**: DVC
- **Experiment Tracking**: MLflow
- **Web Framework**: Flask
- **Containerization**: Docker
- **CI/CD**: Jenkins, GitHub Actions
- **Cloud Platform**: Google Cloud Run (assumed)
- **Monitoring**: Logging integrated with Flask (Prometheus/Grafana can be added)
- **Others**: Pandas, NumPy, Jupyter Notebooks

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Docker
- Git
- Google Cloud SDK (for Google Cloud Run deployment)
- Jenkins (for CI/CD pipeline)
- MLflow server (for experiment tracking)
- DVC (for data versioning)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sanatwalia896/MLOPS_PROJECT.git
   cd MLOPS_PROJECT
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize DVC**:
   ```bash
   dvc init
   dvc pull
   ```

5. **Set Up MLflow**:
   Ensure an MLflow tracking server is running. Update the MLflow tracking URI in `src/model_training.py` if needed:
   ```python
   import mlflow
   mlflow.set_tracking_uri("http://<your-mlflow-server>:5000")
   ```

6. **Set Up Docker** (if running locally):
   Build the Docker image:
   ```bash
   docker build -t hotel-cancellation-prediction .
   ```

---

## Usage

### Running the Flask App Locally
1. Start the Flask application:
   ```bash
   python src/app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000` to access the web interface.
3. Input reservation details to get cancellation predictions.

### Making Predictions via API
Send a POST request to the Flask app:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"lead_time": 30, "arrival_date_year": 2023, "arrival_date_month": 7, ...}' http://127.0.0.1:5000/predict
```

### Running Tests
Run unit and integration tests:
```bash
pytest tests/
```

---

## Dataset
The dataset contains hotel reservation data with features such as:
- `lead_time`: Number of days between booking and arrival
- `arrival_date_year`: Year of arrival
- `arrival_date_month`: Month of arrival
- `stays_in_weekend_nights`: Number of weekend nights
- `stays_in_week_nights`: Number of weekday nights
- `adults`, `children`, `babies`: Number of guests
- `is_canceled`: Target variable (1 for canceled, 0 for not canceled)

The raw dataset is stored in `data/raw/`, and processed data is saved in `data/processed/` using DVC for versioning.

---

## MLOps Pipeline
The project follows a comprehensive MLOps pipeline:
1. **Data Ingestion and Preparation**: 
   - Raw data is cleaned and preprocessed using `src/data_preprocessing.py`.
   - DVC tracks datasets to ensure reproducibility.
2. **Model Development and Training**:
   - Models (e.g., XGBoost, Random Forest) are trained using `src/model_training.py`.
   - MLflow tracks experiments, hyperparameters, and metrics (e.g., accuracy, F1-score).
3. **Model Evaluation**:
   - Models are evaluated using metrics like RMSE, MAE, and F1-score.
   - Cross-validation ensures robustness.
4. **Model Deployment**:
   - The trained model is integrated into a Flask app (`src/app.py`).
   - The app is containerized using Docker.
   - Assumed deployment to Google Cloud Run for scalability.
5. **CI/CD**:
   - Jenkins and GitHub Actions automate testing, building, and deployment.
   - The `Jenkinsfile` defines the pipeline stages.
6. **Monitoring**:
   - Basic logging is implemented in the Flask app.
   - Extendable to Prometheus and Grafana for advanced monitoring.

---

## Model Training
To train the model:
1. Run the preprocessing script:
   ```bash
   python src/data_preprocessing.py
   ```
2. Train the model with MLflow tracking:
   ```bash
   python src/model_training.py
   ```
3. View experiment results in the MLflow UI:
   ```bash
   mlflow ui
   ```
   Navigate to `http://127.0.0.1:5000` to explore logged metrics and artifacts.

---

## Web Application
The Flask-based web app (`src/app.py`) provides:
- A form for users to input reservation details.
- A prediction endpoint (`/predict`) for API-based predictions.
- Logging for tracking requests and errors.

To run the app locally:
```bash
python src/app.py
```

---

## CI/CD Pipeline
The project uses Jenkins for CI/CD, with the pipeline defined in `Jenkinsfile`. Key stages include:
1. **Code Checkout**: Pulls the latest code from GitHub.
2. **Testing**: Runs unit and integration tests using pytest.
3. **Build**: Builds the Docker image.
4. **Push**: Pushes the Docker image to a registry (e.g., Docker Hub).
5. **Deploy**: Deployment to Google Cloud Run.

To set up the CI/CD pipeline:
1. Configure Jenkins with the repository URL.
2. Ensure Docker and Google Cloud SDK are installed on the Jenkins server.
3. Update the `Jenkinsfile` with your Docker registry and Google Cloud Run credentials.

---

## Deployment
The project assumes deployment to Google Cloud Run, a serverless platform for running containerized applications. Steps (assumed):
1. Push the Docker image to a container registry (e.g., Google Container Registry):
   ```bash
   docker tag hotel-cancellation-prediction gcr.io/<project-id>/hotel-cancellation-prediction
   docker push gcr.io/<project-id>/hotel-cancellation-prediction
   ```
2. Deploy to Google Cloud Run:
   ```bash
   gcloud run deploy hotel-cancellation-service \
     --image gcr.io/<project-id>/hotel-cancellation-prediction \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```
3. Access the deployed app via the provided Cloud Run URL.

---

## Monitoring and Logging
- **Logging**: The Flask app logs requests and errors to the console. Logs can be extended to a file or external service (e.g., ELK Stack).
- **Monitoring**: Integrate Prometheus and Grafana for real-time metrics (e.g., response time, error rates). Configuration is not included but can be added.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md) and review [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions or inquiries, contact the project maintainer:
- GitHub: [sanatwalia896](https://github.com/sanatwalia896)
- Email: sanatwalia896@example.com
