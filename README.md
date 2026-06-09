# 🚀 MLOps Project — Vehicle Insurance Data Pipeline

A production-grade **MLOps pipeline** designed to demonstrate end-to-end machine learning workflows for vehicle insurance data. This project highlights real-world practices including data ingestion, validation, transformation, model training, deployment, and CI/CD automation.

---

## 📁 Project Setup & Structure

---

### 🔹 Step 1: Project Template
Initialize the project structure by running:


This creates the required folders and placeholder files.

---

### 🔹 Step 2: Package Management
Configure local package imports using:
- setup.py  
- pyproject.toml  

---

### 🔹 Step 3: Virtual Environment & Dependencies


Verify installation:


---

## 📊 MongoDB Setup & Data Management

---

### 🔹 Step 4: MongoDB Atlas Configuration

- Create a MongoDB Atlas account  
- Set up a free M0 cluster  
- Configure:
  - Username & Password  
  - Network access: 0.0.0.0/0  
- Get the connection string (replace `<password>`)  

---

### 🔹 Step 5: Push Data to MongoDB

- Create `notebook/` folder  
- Add dataset  
- Use `mongoDB_demo.ipynb` to upload data  
- Verify in: Database → Browse Collections  

---

## 📝 Logging, Exception Handling & EDA

---

### 🔹 Step 6: Logging & Exception Handling

- Implement logging module  
- Implement custom exception handling  

Test:


---

### 🔹 Step 7: EDA & Feature Engineering

- Perform analysis in notebook  
- Apply feature engineering for pipeline readiness  

---

## 📥 Data Ingestion

---

### 🔹 Step 8: Data Ingestion Pipeline

- Define MongoDB connection in:
  `configuration.mongo_db_connections.py`

- Implement ingestion in:
  `components/data_ingestion.py`  
  `data_access/`

- Update:
  `entity/config_entity.py`  
  `entity/artifact_entity.py`

Run:


---

### 🔐 Environment Variables

**Bash:**

**PowerShell:**

---

## 🔍 Data Validation, Transformation & Model Training

---

### 🔹 Step 9: Data Validation

- Define schema in:
  `config/schema.yaml`

- Implement validation in:
  `utils/main_utils.py`

---

### 🔹 Step 10: Data Transformation

- Implement:
  `components/data_transformation.py`

- Create:
  `entity/estimator.py`

---

### 🔹 Step 11: Model Training

- Train models in:
  `components/model_trainer.py`

---

---

## 🚀 Model Evaluation, Pusher & Prediction Pipeline

---

### 🔹 Step 12: Model Evaluation & Deployment

- Build evaluation and deployment components  
- Create prediction pipeline  
- Integrate API using `app.py`  

---

### 🔹 Step 13: UI Setup

- Add:
  `static/`  
  `templates/`  

---

## 🔄 CI/CD with Docker, GitHub Actions & HuggingFace

---

### 🔹 Step 14: Docker & GitHub Actions

- Create:
  `Dockerfile`  
  `.dockerignore`

---

### 🔹 Step 16: Hugging Face Setup

- Launch HF spaces  
- Install Docker  
- Connect EC2 as self-hosted runner  

---

### 🔹 Step 18: Deployment Access

- Open port: **5080**

Access application:


---

## 🛠️ Additional Resources

- `crashcourse.txt` → setup.py & pyproject guide  
- GitHub Secrets → secure CI/CD configuration  

---

## 🎯 Project Workflow
- Data Ingestion ➔ Data Validation ➔ Data Transformation
- Model Training ➔ Model Evaluation ➔ Model Deployment
- CI/CD Automation with GitHub Actions, Docker, AWS EC2, and ECR


---

## 💬 Connect

If you found this project helpful or have questions, feel free to reach out!
