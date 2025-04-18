# Shopping Purchase Prediction - Machine Learning Project

## Project Overview

This project aims to build a machine learning model to predict whether a user will make a purchase on an online shopping platform based on their browsing behavior. The model uses the k-nearest neighbor (KNN) algorithm to classify users as either likely to make a purchase or not, based on features such as the number of pages visited, the type of browser, and whether the visit occurred during a weekend.

The model is evaluated using two key metrics:
- **Sensitivity**: The proportion of users who made a purchase and were correctly identified.
- **Specificity**: The proportion of users who did not make a purchase and were correctly identified.

## Table of Contents

- [Project Background](#project-background)
- [Dataset Description](#dataset-description)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Result Interpretation](#result-interpretation)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Contributing](#contributing)

## Project Background

When users visit online shopping websites, not all of them will make a purchase. The objective of this project is to build a machine learning model that can predict whether a user will complete a purchase based on their browsing behavior. This model can help websites target users more effectively, offering incentives or targeted marketing to users predicted to not make a purchase.

The model uses the k-nearest neighbors (KNN) algorithm, a popular classification method. The performance of the model is evaluated using sensitivity and specificity metrics to ensure it performs well across both categories of users (those who purchase and those who do not).

## Dataset Description

The dataset, `shopping.csv`, contains records of user sessions on an online shopping website. Each row corresponds to a user's visit and includes the following features:
- **Browsing Behavior**: The number of pages visited, time spent on each page, bounce rates, and exit rates.
- **User Attributes**: Information such as operating system, browser type, and region.
- **Traffic Information**: Whether the visit was from a direct search or a referral, and whether the visit occurred during the weekend.
- **Outcome**: Whether the user made a purchase (`Revenue`).

## Data Preprocessing

Before training the model, the dataset undergoes several preprocessing steps:
- **Categorical to Numerical Transformation**: Categorical variables such as "Month", "VisitorType", and "Weekend" are converted into numerical values.
- **Feature Selection**: The features relevant to predicting purchases are selected, and any irrelevant or redundant data is removed.
- **Data Splitting**: The dataset is split into training and testing sets for model training and evaluation.

## Model Training

The project uses the **k-nearest neighbors (KNN)** algorithm to classify users based on their browsing behavior. KNN is a simple yet effective method where the class of a user (purchase or no purchase) is predicted based on the classes of the closest training examples.

The model is trained using the training data, and the parameters (such as the number of neighbors) are tuned for optimal performance.

## Evaluation

The model's performance is evaluated based on two important metrics:
- **Sensitivity**: Measures the proportion of users who made a purchase and were correctly identified as buyers.
- **Specificity**: Measures the proportion of users who did not make a purchase and were correctly identified as non-buyers.

These metrics ensure that the model does not just predict the majority class but performs well across both classes (those who make a purchase and those who do not).

## Result Interpretation

After running the model, the results include:
- **Accuracy**: The overall proportion of correct predictions.
- **Sensitivity and Specificity**: These values provide a detailed assessment of the model’s performance, helping understand how well it identifies both buyers and non-buyers.

## Installation Instructions

To run this project, follow these steps:
1. Clone or download the repository containing the project files.
2. Install the necessary dependencies.
   - You will need Python and a few key libraries such as `scikit-learn` for machine learning.
3. Ensure the `shopping.csv` dataset is available in the project directory.

## Usage

To use the model:
1. Place the `shopping.csv` dataset file in the project directory.
2. Run the project by executing the script that processes the data, trains the model, and outputs the results.
3. Review the output, which will include the model’s evaluation metrics (sensitivity, specificity, and accuracy).

## Contributing

Contributions are welcome! Feel free to fork the repository, open issues, and submit pull requests. Suggestions for improving the model, optimizing performance, or adding new features are always appreciated.

---

## License

This project is licensed under the MIT License.

