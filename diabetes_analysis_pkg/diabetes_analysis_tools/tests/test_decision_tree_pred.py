import pytest
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Import the function from your package
from diabetes_analysis_tools.decision_tree_pred import generate_decision_tree_pred

# Creating a binary classification dataset for the tests
X, y = make_classification(n_samples=200, n_features=5, n_informative=3, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


def test_generate_decision_tree_pred_output_length():
    predictions = generate_decision_tree_pred(X_train, y_train, X_test)
    assert len(predictions) == len(X_test), "The number of predictions should match the number of test samples."


def test_generate_decision_tree_pred_output_values():
    predictions = generate_decision_tree_pred(X_train, y_train, X_test)
    assert set(predictions).issubset({0, 1}), "The predictions should only contain 0 and 1 for binary classification."


def test_generate_decision_tree_pred_type():
    predictions = generate_decision_tree_pred(X_train, y_train, X_test)
    assert isinstance(predictions, np.ndarray), "Output should be a numpy array"
