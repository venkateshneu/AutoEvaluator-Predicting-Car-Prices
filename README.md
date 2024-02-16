# AutoEvaluator-Predicting-Car-Prices
![Screenshot 2024-02-15 151206](https://github.com/venkateshneu/AutoEvaluator-Predicting-Car-Prices/assets/141394492/1b72ebda-b78d-472d-a6e0-c7d747078773)

# END TO END ML MODEL: Auto Evaluator: Car Price Predictor
Auto Evaluator: Car Price Predictor 🚗💰

# Project Description 📝
Auto Evaluator: Car Price Predictor is an end-to-end machine learning project aimed at predicting the prices of used cars. Whether you're a buyer seeking a good deal or a seller aiming to set a fair price, this tool provides valuable insights into the estimated price of a car based on various factors.

# Workflow 🔄

# Data Collection 📊
1. Importing necessary libraries: pandas, numpy.
2. Loading the dataset quikr_car.csv containing information about used cars.

# Data Cleaning and Outlier Detection 🧹📊
1. Handling missing values in columns like "kms_driven" and "fuel_type".
2. Converting data types to the appropriate format (e.g., strings to integers for numerical columns like "year" and "Price").
3. Filtering out unrealistic values (e.g., extremely high or low prices) to address outliers.

# Model Building 🛠️🔢
1. Linear Regression: A basic regression model for predicting car prices.
2. Ridge Regression: A regression model with L2 regularization to handle multicollinearity.
3. Lasso Regression: A regression model with L1 regularization for feature selection.

# Model Evaluation and Results 📊
1. Evaluating model performance using metrics like R-squared score.
2. Results: Linear Regression (R-squared: 0.85), Ridge Regression (R-squared: 0.79), Lasso Regression (R-squared: 0.07).

# Model Deployment 🚀🌐
1. Creating a Flask web application for the Car Price Predictor.
2. Designing a user-friendly interface for inputting car details.
3. Utilizing the trained machine learning model to predict car prices and display the predicted price to the user.

# Requirements 📋
1. Python 3.x
2. Libraries: pandas, numpy, scikit-learn, Flask
3. Dataset: quikr_car.csv

# Usage 💻
1. Clone the repository.
2. Install the required Python libraries.
3. Run the Flask web application.
4. Input car details to predict the price.

# Conclusion 🎉🔍
Auto Evaluator: Car Price Predictor provides an end-to-end solution for predicting car prices in the used car market. By leveraging machine learning techniques and deploying a user-friendly web application, it facilitates informed decision-making for both buyers and sellers. The project demonstrates the effectiveness of regression models in estimating car prices based on relevant features, contributing to a more transparent and efficient used car trading process.

