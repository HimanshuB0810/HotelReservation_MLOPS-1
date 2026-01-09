---
title: Hotel Reservation Prediction
emoji: 🏨
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.44.0"
app_file: application.py
pinned: false
---
# Hotel Reservation Prediction – MLOps Project

This project implements an end-to-end MLOps pipeline to predict hotel reservation cancellations. By identifying high-risk bookings early, hotel management can optimize revenue, reduce last-minute vacancies, and mitigate potential booking-related scams.

## 📌 Project Overview

* **Goal**: Develop and deploy a machine learning model to predict the likelihood of reservation cancellations or fraudulent patterns.
* **GitHub Repository**: [https://github.com/HimanshuB0810/HotelReservation_MLOPS-1.git](https://github.com/HimanshuB0810/HotelReservation_MLOPS-1.git)
* **Value Proposition**: Enables revenue management teams and fraud detection units to improve trust and financial planning.

## 🌐 Live Demo

* **Deployment URL**: [https://hotel-reservation-mlops.onrender.com](https://www.google.com/search?q=https://hotel-reservation-mlops.onrender.com)
* **Platform**: Render (Web Service)

## 🎯 Target Audience

* Hotel chains and property owners
* Online travel agencies (OTAs)
* Revenue management teams
* Fraud detection and risk teams

## 💡 How This Project Helps

* **Identifies high-risk reservations early**: Helps in proactive decision-making.
* **Reduces last-minute cancellations**: Minimizes revenue loss from empty rooms.
* **Detects suspicious patterns**: Aids in identifying potentially fraudulent bookings.
* **Improves planning**: Enhances overall revenue planning and customer trust.

## 🛠 Tech Stack

* **Programming Language**: Python
* **Machine Learning**: Scikit-learn, LightGBM
* **Data Manipulation**: Pandas, NumPy
* **Experiment Tracking**: MLflow
* **Object Storage**: MinIO (used for dataset and artifact storage)
* **Containerization**: Docker
* **CI/CD Automation**: Jenkins
* **Web Framework**: Flask

## 🏗 Project Architecture & Pipeline

The project follows a modular pipeline structure:

1. **Data Ingestion**: Fetches raw data from MinIO buckets.
2. **Data Processing**: Handles categorical encoding and numerical scaling for features like `lead_time` and `avg_price_per_room`.
3. **Model Training**: Trains a LightGBM classification model based on key features.
4. **Deployment**: A Flask-based service provides a web interface for real-time predictions.

## 🚀 CI/CD Workflow (Jenkins)

The `Jenkinsfile` automates the following:

* **Cloning**: Pulls the latest code from the GitHub repository.
* **Environment Setup**: Builds a virtual environment and installs dependencies.
* **Build & Push**: Creates a Docker image and pushes it to Docker Hub (`himanshu863/ml-project`).
* **Deployment**: Automatically manages container updates and redeploys the service.

## 📦 How to Run Locally

### Using Docker

```bash
docker pull himanshu863/ml-project:latest
docker run -p 8080:8080 himanshu863/ml-project:latest

```

### Manual Setup

1. Clone the repository: `git clone https://github.com/HimanshuB0810/HotelReservation_MLOPS-1.git`
2. Install dependencies: `pip install -e .`
3. Run the training pipeline: `python pipeline/training_pipeline.py`
4. Start the application: `python application.py`

## 📈 Future Roadmap

* **Real-time Fraud Detection**: Implementation of streaming data analysis.
* **Drift Monitoring**: Integration of tools to monitor model performance over time.
* **Orchestration**: Transitioning to Kubernetes for automated scaling.