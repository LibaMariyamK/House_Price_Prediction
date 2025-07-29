from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_data = {
        'area_sqft': int(request.form['area_sqft']),
        'bedrooms': int(request.form['bedrooms']),
        'bathrooms': float(request.form['bathrooms']),
        'year_built': int(request.form['year_built']),
        'distance_to_city_center': float(request.form['distance_to_city_center']),
        'has_pool': int(request.form['has_pool']),
        'condition': int(request.form['condition']),
        'crime_rate': float(request.form['crime_rate']),
        'school_rating': int(request.form['school_rating']),
    }

    user_df = pd.DataFrame([user_data])
    prediction = model.predict(user_df)[0]
    prediction = round(prediction, 2)

    return render_template('index.html', prediction_text=f'Predicted House Price: ₹{prediction:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)
