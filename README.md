# AutoEvaluator-Predicting-Car-Prices
![Screenshot 2024-02-15 151206](https://github.com/venkateshneu/AutoEvaluator-Predicting-Car-Prices/assets/141394492/1b72ebda-b78d-472d-a6e0-c7d747078773)

# END TO END ML MODEL: Auto Evaluator: Car Price Predictor

Auto Evaluator: Car Price Predictor

Project Description 🚗💰
Welcome to the Auto Evaluator - Car Price Predictor project! This project aims to predict the prices of used cars using machine learning techniques. Whether you're a buyer looking for a good deal or a seller trying to set a fair price, this tool will provide valuable insights into the estimated price of a car based on various factors.

Requirements 📋
Python 3.x
pandas
numpy
scikit-learn
Flask (for web application deployment)
Data Cleaning and Outlier Detection 🧹📊
The project begins by importing the necessary libraries like pandas and numpy. We load the dataset (quikr_car.csv) containing information about used cars. Then, we focus on cleaning the data and detecting outliers to ensure the reliability of our predictive models.

Cleaning the Data 🛠️
We address missing values and inconsistent data types in the dataset. This involves:

Handling missing values in columns like "kms_driven" and "fuel_type".
Converting data types to the appropriate format, such as converting strings to integers for numerical columns like "year" and "Price".
Outlier Detection 🚨
Outliers can significantly impact the performance of machine learning models. Therefore, we employ techniques to identify and handle outliers in the dataset:

We filter out rows with unrealistic values, such as extremely high or low prices, which may indicate data entry errors.
Additionally, we remove entries with improbable values in the "kms_driven" column, ensuring that only realistic data points are considered for model training.
Model Building 🛠️🔢
With a clean dataset free of outliers, we proceed to build machine learning models for predicting car prices. The models used include:

Linear Regression: A basic regression model used for predicting car prices based on input features.

Ridge Regression: A regression model with L2 regularization to handle multicollinearity in the dataset.

Lasso Regression: A regression model with L1 regularization for feature selection and sparsity in coefficients.

Model Evaluation and Results 📊
We evaluate the performance of each model using metrics like R-squared score, which measures the proportion of the variance in the target variable that is predictable from the input features. The results are as follows:

Linear Regression: R-squared score of 0.85
Ridge Regression: R-squared score of 0.79
Lasso Regression: R-squared score of 0.07 (with a convergence warning)
Model Deployment 🚀🌐
We create a Flask web application for the Car Price Predictor, designing a user-friendly interface for inputting car details. The trained machine learning model is utilized to predict car prices, and the predicted price is displayed to the user on the web page.

Conclusion 🎉🔍
The Auto Evaluator - Car Price Predictor project provides an end-to-end solution for predicting car prices in the used car market. By leveraging machine learning techniques and deploying a user-friendly web application, it facilitates informed decision-making for both buyers and sellers. The project demonstrates the effectiveness of regression models in estimating car prices based on relevant features, contributing to a more transparent and efficient used car trading process.
