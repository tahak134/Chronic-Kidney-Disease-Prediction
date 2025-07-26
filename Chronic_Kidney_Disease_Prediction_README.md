
# Chronic Kidney Disease Prediction

## Project Overview
This project aims to predict **Chronic Kidney Disease (CKD)** in patients based on various health-related features such as age, blood pressure, specific gravity, and other biomarkers. The project demonstrates an end-to-end **MLOps pipeline**, leveraging cloud infrastructure, model experimentation, deployment, and monitoring.

## Problem Description
Chronic Kidney Disease is a global health issue that affects millions of people worldwide. Early detection of CKD can help in **preventive care**, reducing long-term healthcare costs and improving patient quality of life. This project uses a machine learning approach to predict whether a patient is at risk of CKD based on medical data.

## Problem the Project Solves
This project provides a solution for early detection of Chronic Kidney Disease by:
- **Predicting CKD status** based on a variety of health-related features.
- **Improving healthcare outcomes** through machine learning-based prediction models.
- **Making the solution scalable** through deployment in the cloud with continuous retraining and monitoring for model drift.

## Dataset Description
- **Dataset**: The dataset contains **medical data** of patients with features like age, blood pressure, specific gravity, albumin, and other health indicators.
- **Target variable**: The target variable is **Class** (0 = No CKD, 1 = CKD).
- **Source**: The dataset can be found on Kaggle: [Chronic Kidney Disease Prediction Dataset](https://www.kaggle.com/datasets)

### Features in the Dataset:
- **bp**: Blood Pressure
- **sg**: Specific Gravity
- **al**: Albumin
- **age**: Age of the patient
- **su**: Sugar
- **rbc**: Red Blood Cells
- **pc**: Pus Cell
- **pcc**: Pus Cell Clumps
- **ba**: Bacteria
- **class**: Target variable (CKD or not)

## Technologies Used
- **Cloud**: AWS for cloud deployment
- **Modeling**: XGBoost, Random Forest, Logistic Regression
- **Experiment Tracking**: MLflow
- **Deployment**: Docker, FastAPI, Kubernetes (TBD)
- **Workflow Orchestration**: **Airflow** (recommended) or **Evidently** for monitoring (optional)
- **CI/CD**: GitHub Actions

## Features
- **End-to-end MLOps** pipeline from data preprocessing to model deployment.
- **Cloud-based deployment** and Infrastructure as Code (IaC) for provisioning.
- **Model experimentation** with version control using **MLflow**.
- **Automated retraining pipeline** using **Airflow** to ensure continuous learning and model updates.
- **Model monitoring** with **Evidently** that tracks performance and model drift.

## How to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/chronic-kidney-disease-prediction.git
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the model training**:
   ```bash
   python train_model.py
   ```
4. **Deploy the model** (if using Docker):
   ```bash
   docker build -t ckd-model .
   docker run -p 8000:8000 ckd-model
   ```

5. **For cloud deployment**: Refer to the `cloud_deployment` directory for cloud setup and provisioning using IaC tools.

## Project Structure
```
.
├── data/                    # Raw and processed data
├── src/                     # Source code for data preprocessing, model training, and evaluation
│   ├── train_model.py       # Training the machine learning model
│   ├── preprocess.py        # Data preprocessing functions
│   ├── model.py             # Model implementation (XGBoost, Random Forest)
│   └── predict.py           # Prediction API
├── cloud_deployment/        # Cloud infrastructure setup (Terraform/CloudFormation)
├── docker/                  # Dockerfile for containerization
├── requirements.txt         # List of dependencies
└── README.md                # Project overview and setup instructions
```

## Best Practices Followed
- **Unit Tests**: Ensures the correctness of individual components.
- **Integration Tests**: Validates the interaction between multiple modules.
- **Code Formatting**: Using a linter and formatter for consistency.
- **CI/CD Pipeline**: Automated model retraining and deployment via GitHub Actions.
- **Version Control**: Experiment tracking and model registry using **MLflow**.

## Model Monitoring
This project uses **Evidently** to monitor the performance of deployed models. The monitoring tracks:
- Model accuracy
- Drift detection
- Alerts for performance degradation and retraining triggers.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
