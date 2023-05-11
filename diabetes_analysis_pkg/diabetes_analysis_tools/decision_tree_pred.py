
def generate_decision_tree_pred(X_train, y_train, X_test):
    """
    This function standardizes the training and testing data, 
    fits a Decision Tree Classifier with a max depth of 3 on the training data, 
    and returns predictions on the testing data.

    Parameters:
    X_train: DataFrame containing the training predictors
    y_train: Series containing the training response variable
    X_test: DataFrame containing the testing predictors

    Returns:
    dt_model_pred: Series of predictions on the testing data
    """
    
    # Instantiate a StandardScaler object
    scaler = StandardScaler()
    
    # Fit the scaler to the training data and transform both training and testing data
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Instantiate a Decision Tree Classifier model with max_depth=3
    dt_model = DecisionTreeClassifier(max_depth = 3)
    
    # Fit the model to the training data
    dt_model.fit(X_train, y_train)
    
    # Predict the testing data
    dt_model_pred = dt_model.predict(X_test)
    
    # Return the predictions
    return dt_model_pred
