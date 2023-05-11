import pytest
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from diabetes_analysis_tools.logistic_pred import generate_logistic_pred

# from your_module import generate_logistic_pred


# Create some synthetic binary classification data
X, y = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


def test_generate_logistic_pred_output_length():
    predictions = generate_logistic_pred(X_train, y_train, X_test)
    assert len(predictions) == len(X_test), "The number of predictions should match the number of test samples."


def test_generate_logistic_pred_output_values():
    predictions = generate_logistic_pred(X_train, y_train, X_test)
    assert set(predictions).issubset({0, 1}), "The predictions should only contain 0 and 1 for binary classification."