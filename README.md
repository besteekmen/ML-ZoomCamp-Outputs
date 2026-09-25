# Machine Learning Zoomcamp 2026 — Course Work & Projects

This repository contains my personal notes, code, hands-on module exercises, homework assignments, and projects for the **[Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp)**, a free practical machine learning engineering course organized by **[DataTalks.Club](https://datatalks.club/)**.

The course follows the complete machine learning workflow: framing a problem, preparing data, training and evaluating models, exposing predictions through APIs, packaging services, and deploying machine learning systems.

My goal with this repository is to document both the concepts covered during the course and my own implementation work as I progress through the 2026 cohort.

---

## ⚙️ Setup

This repository uses **`uv`** for Python version and dependency management.

Detailed setup instructions are available in:

➡️ **[SETUP.md](./SETUP.md)**

The setup guide covers two scenarios:

* **Initial project setup** — creating the Python project and environment from scratch.
* **Setup after cloning the repository** — recreating the environment on a new machine, WSL installation, Codespace, or other development environment using the existing `pyproject.toml`, `uv.lock`, and `.python-version`.

For an already cloned repository, the environment can generally be recreated with:

```bash
uv python install
uv sync
```

The local `.venv` directory is not committed to Git and can be reproduced from the project configuration files.

---

## 📂 Repository Structure

The repository is organized according to the ML Zoomcamp course modules. Each module contains my lecture notes, code, exercises, and homework assignments.

### Core Machine Learning

* 📂 **[Module 1: Introduction to Machine Learning](./module1_intro/)**
  Machine learning fundamentals, supervised learning, CRISP-DM, model selection, and development environment setup.

* 📂 **[Module 2: Machine Learning for Regression](./module2_regression/)**
  Linear regression, exploratory data analysis, feature engineering, regularization, validation, and model tuning.

* 📂 **[Module 3: Machine Learning for Classification](./module3_classification/)**
  Logistic regression, categorical encoding, feature importance, model interpretation, feature selection, and customer churn prediction.

* 📂 **[Module 4: Evaluation Metrics for Classification](./module4_evaluation/)**
  Accuracy, precision, recall, F1 score, confusion matrices, ROC curves, AUC, cross-validation, threshold selection, and evaluation of imbalanced classification problems.

### Deployment & Tree-Based Models

* 📂 **[Module 5: Deploying Machine Learning Models](./module5_deployment/)** — *Coming soon*
  Model serialization, prediction services, FastAPI, Docker, and deploying machine learning models as web services.

* 📂 **[Module 6: Decision Trees and Ensemble Learning](./module6_trees/)** — *Coming soon*
  Decision trees, random forests, gradient boosting, XGBoost, feature importance, and hyperparameter tuning.

### Project

* 🚀 **[Midterm Project](./midterm-project/)** — *Coming soon*
  An end-to-end machine learning project applying the concepts from Modules 1–6, including data preparation, model development, evaluation, and deployment.

### Deep Learning & Production ML

* 📂 **[Module 8: Neural Networks and Deep Learning](./module8_deep_learning/)** — *Coming soon*
  Neural network fundamentals, PyTorch, TensorFlow/Keras, convolutional neural networks, transfer learning, and image classification.

* 📂 **[Module 9: Serverless Deep Learning](./module9_serverless/)** — *Coming soon*
  Serverless machine learning deployment using AWS Lambda, API Gateway, and deployment of both classical ML and deep learning models.

* 📂 **[Module 10: Kubernetes and TensorFlow Serving](./module10_kubernetes/)** — *Coming soon*
  Kubernetes fundamentals for machine learning, TensorFlow Serving, scalable model serving, service deployment, and traffic distribution.

* 📂 **[Module 11: KServe](./module11_kserve/)** — *Coming soon*
  Model serving with KServe and Kubernetes-based inference infrastructure.

### Final Projects

* 🚀 **[Capstone Project 1](./capstone-project/)** — *Coming soon*
  A larger end-to-end machine learning engineering project bringing together model development, evaluation, deployment, and production-oriented ML concepts.

* 🚀 **Capstone Project 2** — *Optional / Coming later*
  An optional second capstone project for further practice with the complete machine learning lifecycle.

> Additional notebooks, homework assignments, project files, and supporting materials will be added as I progress through the course.

---

## 🎯 What I'm Learning & Building

Throughout the course, I am building hands-on experience across the complete machine learning lifecycle.

* **Machine Learning Fundamentals:** Understanding the ML workflow, problem formulation, supervised learning, model selection, and working with real-world datasets.

* **Regression & Classification:** Building predictive models using linear regression, logistic regression, and scikit-learn.

* **Feature Engineering:** Preparing data, encoding categorical variables, selecting useful features, and improving model performance.

* **Model Evaluation:** Evaluating models using accuracy, precision, recall, F1 score, ROC/AUC, confusion matrices, cross-validation, and threshold analysis.

* **Tree-Based Models:** Working with decision trees, random forests, gradient boosting, and XGBoost.

* **Deep Learning:** Building neural networks and image-classification systems using PyTorch and TensorFlow/Keras.

* **Model Deployment:** Turning trained models into prediction services using FastAPI and Docker.

* **Cloud & Serverless ML:** Deploying machine learning and deep learning models using AWS Lambda and related cloud services.

* **Scalable Model Serving:** Learning how to serve and scale models using Kubernetes, TensorFlow Serving, and KServe.

* **Reproducible Environments:** Managing Python versions, dependencies, virtual environments, and lock files using `uv`.

* **End-to-End ML Engineering:** Taking a machine learning problem from data preparation and experimentation through evaluation, deployment, and production-style serving.

---

## 🚀 Projects

Projects are an important part of ML Zoomcamp because they combine the individual techniques learned in the modules into complete machine learning systems.

### Midterm Project

The midterm project applies the material from the first six modules to an end-to-end machine learning problem.

The project includes tasks such as:

* selecting and exploring a dataset,
* defining the machine learning problem,
* preparing and engineering features,
* training and comparing models,
* evaluating model performance,
* exposing predictions through a service,
* and deploying the resulting application.

📌 **Project details coming soon.**

### Capstone Project

The capstone project is a larger machine learning engineering project completed after the main course modules.

It brings together the complete ML workflow, including:

* data preparation,
* experimentation,
* model development,
* evaluation,
* deployment,
* and production-oriented serving.

📌 **Project details coming soon.**

---

## 🛠️ Technologies & Tools

Throughout the course, I will work with technologies including:

* **Python**
* **NumPy**
* **pandas**
* **Matplotlib**
* **Seaborn**
* **scikit-learn**
* **XGBoost**
* **PyTorch**
* **TensorFlow / Keras**
* **FastAPI**
* **Docker**
* **AWS Lambda**
* **Kubernetes**
* **TensorFlow Serving**
* **KServe**
* **Jupyter**
* **uv**
* **Git & GitHub**

---

## 📚 Course Resources

* **[ML Zoomcamp GitHub Repository](https://github.com/DataTalksClub/machine-learning-zoomcamp)**
* **[DataTalks.Club](https://datatalks.club/)**
* **[ML Zoomcamp Course Platform](https://courses.datatalks.club/ml-zoomcamp-2026/)**

The official course repository contains the lectures, notebooks, homework materials, project requirements, and supporting resources for the course.

---

## 🤝 Connect with Me

* **GitHub:** [@besteekmen](https://github.com/besteekmen)
* **LinkedIn:** [Beste Ekmen](https://linkedin.com/in/besteekmen)
* **Slack:** Find me in the DataTalksClub `#course-ml-zoomcamp` channel.
