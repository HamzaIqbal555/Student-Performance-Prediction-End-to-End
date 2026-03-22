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

\n\n## 🌐 Live Demo & API\n**Production API for testing predictions!** (Google Cloud Run)\n\n**Base URL**: https://student-performance-prediction-end-to-end-393040721523.europe-west1.run.app/\n\n**Test the Predictor**:\nUse POST `/predict` with JSON payload (inputs: gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score).\n\n**Example curl**:\n```bash\ncurl -X POST https://student-performance-prediction-end-to-end-393040721523.europe-west1.run.app/predict \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\n    \"gender\": \"male\",\n    \"race_ethnicity\": \"group B\",\n    \"parental_level_of_education\": \"bachelor\\u0027s degree\",\n    \"lunch\": \"standard\",\n    \"test_preparation_course\": \"none\",\n    \"reading_score\": 72,\n    \"writing_score\": 74\n  }'\n```\nReturns: `{\"predicted_average_score\": <value>}`\n\n\n## 🔮 How it Works
1. **Data** → EDA in notebooks.
2. **Train**: Pipelines ingest/transform/train (CatBoost > others).
3. **Predict**: Load model/preprocessor → Scale inputs → Predict.

Built with ❤️ for learning ML deployment!


