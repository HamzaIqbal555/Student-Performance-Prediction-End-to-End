from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData
from src.pipeline.predict_pipeline import PredictPipeline
from google.cloud import bigquery
from datetime import datetime

application = Flask(__name__)
app = application

# testing auto deployment
# BigQuery setup
BQ_CLIENT = bigquery.Client()
BQ_TABLE = "student-ml-project.student_predictions.predictions"


def log_prediction_to_bigquery(input_data, prediction):
    """Log prediction inputs and results to BigQuery"""
    rows = [{
        "timestamp": datetime.utcnow().isoformat(),
        "gender": input_data.gender,
        "race_ethnicity": input_data.race_ethnicity,
        "parental_level_of_education": input_data.parental_level_of_education,
        "lunch": input_data.lunch,
        "test_preparation_course": input_data.test_preparation_course,
        "reading_score": input_data.reading_score,
        "writing_score": input_data.writing_score,
        "predicted_score": float(prediction)
    }]

    errors = BQ_CLIENT.insert_rows_json(BQ_TABLE, rows)
    if errors:
        print(f"BigQuery logging error: {errors}")
    else:
        print("Prediction logged to BigQuery successfully!")


@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get(
                'parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get(
                'test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        pred_df = data.get_data_as_dataframe()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Log prediction to BigQuery
        log_prediction_to_bigquery(data, results[0])

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'results': results[0]})
        return render_template('home.html', results=results[0])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
