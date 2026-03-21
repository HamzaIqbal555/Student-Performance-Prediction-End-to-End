# 📊 Student Performance Predictor

## 🎯 What is this?
A simple **web app** that predicts a student's **average exam score** (math + reading + writing) using Machine Learning. Built with **Flask**, **CatBoost**, and follows full ML lifecycle (EDA → Training → Deployment). Perfect for beginners!

**Dataset**: Kaggle [Students Performance](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) (1000 students).
- **Inputs**: Gender, ethnicity, parental education, lunch type, test prep course, reading/writing scores.
- **Output**: Predicted average score.

## 🚀 Features
- Interactive web UI for predictions (form + AJAX).
- **CatBoost Regressor** (best: **R² = 0.88** on test set, beats XGB 0.85, RF 0.85).
- Production-ready: Dockerized, artifacts saved.
- Notebooks for EDA & training.

**Model Comparison** (Test R²):
| Model       | R² Score |
|-------------|----------|
| CatBoost   | 0.8806  |
| Ridge      | 0.8806  |
| XGB        | 0.8516  |
| RF         | 0.8514  |

## 📁 Project Structure
```
ML_Project/
├── artifacts/          # Model, preprocessor, data
├── notebook/           # EDA.ipynb, training.ipynb
├── src/
│   ├── components/     # Data ingestion, transformation, trainer
│   └── pipeline/       # Train & predict pipelines
├── templates/          # HTML pages (home.html)
├── static/             # CSS/JS
├── application.py      # Flask app
├── Dockerfile          # Deployment
└── requirements.txt
```

## 🛠️ Quick Start (Local)
1. Install deps: `pip install -r requirements.txt`
2. Run app: `python application.py`
3. Open http://localhost:5000
4. Fill form → Get prediction!

## 🐳 Docker
```bash
docker build -t ml-student-predictor .
docker run -p 5000:5000 ml-student-predictor
```

## 🔮 How it Works
1. **Data** → EDA in notebooks.
2. **Train**: Pipelines ingest/transform/train (CatBoost > others).
3. **Predict**: Load model/preprocessor → Scale inputs → Predict.

Built with ❤️ for learning ML deployment!


