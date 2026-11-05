# ♻️ Smart Waste Classification

A machine learning web app that predicts a waste category — **Plastic, Paper, Glass,
Metal, or Organic** — from six measured characteristics, using a Random Forest
classifier and an interactive Streamlit dashboard.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Anojpawar/Waste-classification)

## Features

- Random Forest model (200 trees) with median imputation in a scikit-learn pipeline
- Dashboard showing dataset class distribution, accuracy, precision, recall, F1-score
  and the confusion matrix
- Prediction form with input validation for all six features
- Self-healing startup: if `waste_model.pkl` is missing or was built with a different
  scikit-learn version, the app retrains automatically
- Smoke tests that train the model and click through a prediction in the dashboard

## Tech stack

Python · pandas · NumPy · scikit-learn · Streamlit · Render

## Project structure

```
├── app.py                               # Streamlit dashboard
├── train.py                             # Training + evaluation, saves waste_model.pkl
├── smart_waste_classification_500.csv   # Dataset (500 synthetic samples)
├── tests/test_app.py                    # Smoke tests (training + dashboard prediction)
├── requirements.txt
└── render.yaml                          # One-click Render deployment config
```

## Dataset

`smart_waste_classification_500.csv` contains these columns:

| Column | Description |
| --- | --- |
| `sample_id` | Identifier (not used for training) |
| `weight_g` | Weight in grams |
| `moisture_pct` | Moisture percentage (0–100) |
| `hardness_1_to_10` | Hardness on a 1–10 scale |
| `density_g_cm3` | Density in g/cm³ |
| `transparency_score` | Transparency (0–1) |
| `conductivity_score` | Electrical conductivity (0–1) |
| `waste_category` | Prediction target |

> The 500 samples are **synthetic**. They demonstrate the ML workflow, but the test
> metrics do not represent real-world waste classification performance.

## Run locally

```bash
python -m venv .venv
# Windows: .\.venv\Scripts\Activate.ps1    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

python train.py              # train, print metrics, save waste_model.pkl
streamlit run app.py         # open http://localhost:8501
```

Run the tests:

```bash
pip install pytest
python -m pytest -v
```

## Model and evaluation

The target is `waste_category`; `sample_id` is excluded. Training uses an 80/20
stratified train/test split with random seed 42 and reports accuracy plus weighted
precision, recall and F1-score, along with a confusion matrix.

## Deploy

Click the **Deploy to Render** button above, or create a Blueprint on
[Render](https://render.com) from this repo — `render.yaml` configures a free web service.

- Build command: `pip install -r requirements.txt && python train.py`
- Start command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
