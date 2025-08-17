# 🩺 Chronic Kidney Disease Prediction  

This project is a **machine learning application** for predicting Chronic Kidney Disease (CKD) based on patient health data.  
It uses **FastAPI** as the backend framework, with a trained ML model to serve predictions via REST API.  

---

## 📂 Project Structure  

```
chronic-kidney-disease-pred/
│
├── api/
│   ├── main.py          # FastAPI application entrypoint
│   ├── model.pkl        # Trained machine learning model
│   ├── requirements.txt # Python dependencies
│
├── notebooks/           # Jupyter notebooks for EDA & training
├── data/                # (Optional) raw and processed datasets
├── Dockerfile           # Containerization for cloud deployment
├── .gitignore           # Ignored files (env, data, etc.)
└── README.md            # Project documentation
```

---

## ⚙️ Installation  

### Prerequisites
- Python 3.9+  
- pip / conda  
- (Optional) Docker  

### Setup Locally  

1. Clone the repository:  
   ```bash
   git clone https://github.com/tahak134/Chronic-Kidney-Disease-Prediction.git
   cd Chronic-Kidney-Disease-Prediction
   ```

2. Create a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the API  

From the project root, run:  

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be live at:  
👉 http://13.53.123.119/docs

---

## 📡 API Endpoints  

### **Root**  
`GET /` → Health check, confirms API is running  

### **Prediction**  
`POST /predict`  

**Request Body Example:**  
```json
{
  "age": 45,
  "bp": 80,
  "sg": 1.02,
  "al": 1,
  "su": 0,
  "bgr": 121,
  "bu": 36,
  "sc": 1.2,
  "sod": 137,
  "pot": 4.5,
  "hemo": 15,
  "pcv": 44,
  "wbcc": 6700,
  "rbcc": 4.9
}
```

**Response Example:**  
```json
{
  "prediction": "1"   #CKD
}
```

---

## 🐳 Running with Docker  

1. Build image:  
   ```bash
   docker build -t ckd-app .
   ```

2. Run container:  
   ```bash
   docker run -p 8000:8000 ckd-app
   ```

---

## ☁️ Deployment  

This project can be deployed to:  
- **AWS EC2** (with Docker)  
- **Heroku / Render** (for free hosting)  
- **AWS ECS / EKS** for scaling  

Steps for **AWS EC2**:  
1. Launch an EC2 instance (Ubuntu recommended).  
2. SSH into the instance.  
3. Install Docker & Git.  
4. Clone this repo.  
5. Build and run container as above.  
6. Open port `8000` in Security Groups.  

---

## 📊 Model Training  

- The ML model was trained using scikit-learn on Chronic Kidney Disease dataset (UCI).  
- Preprocessing includes handling missing values, scaling, and categorical encoding.  
- Model evaluation metrics: Accuracy, F1-score, ROC-AUC.  

---

## 👨‍💻 Author  

**Taha K.**  
📧 taha.khn70@gmail.com  
🔗 [GitHub](https://github.com/tahak134)  
