Streamlit app: https://telecom-churn-predictions.streamlit.app/

Project Overview

This project analyzes customer churn data and builds a machine learning model to predict whether a customer is likely to leave. The objective is to identify high-risk customers and support retention-focused business decisions.

The workflow is split into:

Exploratory Data Analysis (EDA)

Model training and hyperparameter tuning using GridSearchCV

Dataset Summary

Total samples: 7,042 customers

Target variable: Churn

Class imbalance present

Non-churn customers dominate the dataset

Churn customers represent roughly 25 to 30 percent

The dataset includes:

Demographics

Service subscriptions

Contract and billing information

Monthly and total charges

Exploratory Data Analysis Highlights

Key findings from EDA:

Month-to-month contract customers show the highest churn counts

Customers without OnlineSecurity or TechSupport churn significantly more

Electronic check payment users have the highest churn

Long-term contracts (1 year, 2 year) show strong retention

Gender has minimal impact on churn

These patterns align with real-world telecom churn behavior and informed feature selection.

Model Training Approach

The modeling pipeline includes:

Column-wise preprocessing using ColumnTransformer

One-hot encoding for categorical features

Train-test split with stratification

Logistic Regression model

Hyperparameter tuning using GridSearchCV

5-fold Stratified Cross-Validation

Scoring optimized for Average Precision

The final model is saved as:

churn_model.pkl

Model Performance (Test Set)

Evaluation performed on 1,409 test samples.

Classification Report
Class 0 (Non-Churn):
Precision: 0.94
Recall:    0.80
F1-score:  0.87
Support:   1035

Class 1 (Churn):
Precision: 0.62
Recall:    0.89
F1-score:  0.73
Support:   374

Overall Metrics

Accuracy: 82.4%

ROC AUC Score: 0.93

Average Precision Score: 0.83

Interpretation of Results

The model achieves high recall for churn customers (89%), which is critical for retention use cases

Precision for churn is lower (62%), indicating some false positives, which is acceptable in churn prevention

ROC AUC of 0.93 indicates excellent class separation

Average Precision of 0.83 confirms strong performance on an imbalanced dataset

This model prioritizes catching churners over minimizing false alarms, which aligns with business objectives.

Business Takeaways

High-risk churn customers are typically:

On month-to-month contracts

Paying via electronic check

Lacking support or security services

Early in their customer lifecycle

Retention strategies should focus on these segments first.

Tools and Libraries

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Future Improvements

Feature importance and coefficient analysis

Cost-sensitive learning

Ensemble models (Random Forest, XGBoost)

Probability threshold optimization













 
