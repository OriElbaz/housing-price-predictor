# Housing Price Predictor

## Description

This project is a machine learning application designed to predict housing prices. It features a Multiple Linear Regression model built entirely from scratch using Python and NumPy. The core learning mechanism utilises a vectorised Batch Gradient Descent algorithm to minimise Mean Squared Error, ensuring efficient computation.

The model includes advanced optimisations such as feature scaling and hyperparameter tuning to ensure stability, preventing common issues like gradient oscillation and divergence. The trained model is served via a Flask API, allowing external applications to request price predictions programmatically.

## Key Features

* **Linear Regression from Scratch:** Implementation of the core regression algorithm without relying on high level abstraction libraries.
* **Vectorised Batch Gradient Descent:** Optimised mathematical operations for faster training performance.
* **Mean Squared Error Minimisation:** Custom loss function implementation to guide model accuracy.
* **Feature Scaling:** Data preprocessing to normalise input variables for stable convergence.
* **Hyperparameter Tuning:** Optimised learning rates and iteration counts to improve model reliability.
* **Flask API Integration:** A RESTful interface to expose the model for real time predictions.

## Technologies Used

* Python
* NumPy
* Flask

## Installation

1. Ensure Python is installed on your system.
2. Install the required dependencies using pip:
`pip install numpy flask`

## Usage

1. **Train the Model:** Run the training script to process the dataset and generate the model weights.
2. **Start the Server:** Launch the Flask application to serve the API.
`python app.py`
3. **Make Predictions:** Send JSON data containing housing features to the API endpoint to receive a predicted price.

## API Reference

**Endpoint:** `/predict`
**Method:** POST
**Payload:** JSON object containing feature values (e.g., square footage, number of bedrooms).
**Response:** JSON object containing the estimated housing price.

## Ori Elbaz

Developed on Thu 25 Dec 2025.
