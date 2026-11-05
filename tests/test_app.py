"""Smoke tests: train the model, then render the dashboard and run a prediction."""

from pathlib import Path

from streamlit.testing.v1 import AppTest

import train

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")


def test_training_saves_model_bundle():
    train.train_model()
    assert train.MODEL_PATH.is_file()


def test_dashboard_renders_and_predicts():
    app = AppTest.from_file(APP_PATH, default_timeout=120).run()
    assert not app.exception
    assert not app.error
    assert app.title[0].value == "Smart Waste Classification"
    assert len(app.metric) == 4

    app.button[0].click().run()
    assert not app.exception
    assert app.success, "Expected a prediction result"
    assert "Predicted waste category" in app.success[0].value
