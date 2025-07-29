# 🏠 House Price Prediction

This project is a **House Price Prediction Web App** built using **Flask** and a **Linear Regression model**. The app predicts the price of a house based on user input features such as area, number of bedrooms, bathrooms, etc.

## 📁 Project Structure

```
house_price_prediction/
│
├── app.py                  # Flask app for model deployment
├── house.csv               # Dataset used for training
├── model.ipynb             # Notebook containing data preprocessing & model building
├── model.pkl               # Saved trained model
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # HTML template for the web interface
```

---

## 🧠 Model Summary

* **Model Used:** Linear Regression
* **Training Strategy:**

  * Initial baseline model using numerical features
  * Tried encoding and scaling – no significant improvement
  * Feature selection based on correlation
  * Final model trained on selected features

### 📊 Final Model Metrics:

* **Mean Absolute Error (MAE):** 17,610.82
* **Mean Squared Error (MSE):** 519,923,795.93
* **Root Mean Squared Error (RMSE):** 22,801.84
* **R² Score:** 0.9841

---

## 🧾 Input Features

| Feature                   | Type  | Description                    |
| ------------------------- | ----- | ------------------------------ |
| `area_sqft`               | int   | Total area in square feet      |
| `bedrooms`                | int   | Number of bedrooms             |
| `bathrooms`               | float | Number of bathrooms            |
| `year_built`              | int   | Year the house was built       |
| `distance_to_city_center` | float | Distance to city center (km)   |
| `has_pool`                | int   | 1 if house has pool, else 0    |
| `condition`               | int   | Condition rating (1 to 5)      |
| `crime_rate`              | float | Crime rate in the area         |
| `school_rating`           | int   | Nearby school rating (1 to 10) |

---

## 📌 Notes

* The best-performing model was selected based on R² and error metrics.
* The model was saved using `joblib` and loaded during Flask runtime.
* UI is simple and user-friendly, allowing input and displaying predictions.

---

