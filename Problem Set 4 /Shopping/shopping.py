import csv
import sys

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename: str) -> tuple:
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence (features) should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels (target), where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    shopping_data = pd.read_csv(filename)

    binary_mapping = {
        True: 1,
        False: 0
    }

    shopping_data["Month"] = shopping_data["Month"].map({
        "Jan": 0,
        "Feb": 1,
        "Mar": 2,
        "Apr": 3,
        "May": 4,
        "June": 5,
        "Jul": 6,
        "Aug": 7,
        "Sep": 8,
        "Oct": 9,
        "Nov": 10,
        "Dec": 11
    })

    shopping_data["VisitorType"] = shopping_data["VisitorType"].map({
        "Returning_Visitor": 1,
        "New_Visitor": 0,
        "Other": 0
    })

    shopping_data["Weekend"] = shopping_data["Weekend"].map(binary_mapping)

    shopping_data["Revenue"] = shopping_data["Revenue"].map(binary_mapping)

    #print(shopping_data.dtypes)

    target = shopping_data["Revenue"].values.tolist()
    features = shopping_data.drop(["Revenue"], axis=1).values.tolist()

    return (features, target)


def train_model(evidence, labels):
    """
    Given a list of evidence (features) lists and a list of labels (target), return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    
    See https://en.wikipedia.org/wiki/Sensitivity_and_specificity
    """
    true_positives = 0
    true_negatives = 0

    for label, prediction in zip(labels, predictions):
        if prediction == 1:
            if label == 1: 
                true_positives += 1
        
        if prediction == 0:
            if label == 0:
                true_negatives += 1

    sensitivity = true_positives / labels.count(1)
    specificity = true_negatives / labels.count(0)


    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
