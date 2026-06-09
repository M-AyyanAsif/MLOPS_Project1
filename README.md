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

## 🌐 AWS Setup for Model Evaluation & Deployment

---

### 🔹 Step 12: AWS Setup

- Create IAM user with AdministratorAccess  

Set environment variables:

- Configure S3 access in:
  `constants/__init__.py`

---

### 🔹 Step 13: Model Storage (S3)

- Create S3 bucket:
  `my-model-mlopsproj (us-east-1)`

- Implement:
  `src/aws_storage/`  
  `entity/s3_estimator.py`

---

## 🚀 Model Evaluation, Pusher & Prediction Pipeline

---

### 🔹 Step 14: Model Evaluation & Deployment

- Build evaluation and deployment components  
- Create prediction pipeline  
- Integrate API using `app.py`  

---

### 🔹 Step 15: UI Setup

- Add:
  `static/`  
  `templates/`  

---

## 🔄 CI/CD with Docker, GitHub Actions & AWS

---

### 🔹 Step 16: Docker & GitHub Actions

- Create:
  `Dockerfile`  
  `.dockerignore`

- Configure GitHub Secrets:
  - AWS_ACCESS_KEY_ID  
  - AWS_SECRET_ACCESS_KEY  
  - AWS_DEFAULT_REGION  
  - ECR_REPO  

---

### 🔹 Step 17: AWS EC2 & ECR

- Launch EC2 instance  
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
