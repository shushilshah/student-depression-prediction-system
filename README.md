# 🧠 Student Depression Prediction App

A machine learning web application built using **Streamlit** that predicts whether a student is likely suffering from depression based on their lifestyle factors and academic background.

This project includes:

- An end-to-end **ML pipeline** (training & transformation)
- **MongoDB Atlas** integration to store predictions.
- **Streamlit** UI application to take user input.

---

## 🚀 Features

- User-friendly form for input
- Predicts if a person is likely depressed or not
- Saves prediction history in MongoDB
- Dynamic model training feature.

---

## 📊 Tech Stack

- **Python**
- **Scikit-learn**, **Pandas**, **Joblib**
- **Streamlit**
- **MongoDB Atlas** (Cloud Database)

---

## ⚙️ Setup Instructions

### 1. 🔑 Environment Setup

Create a `.env` file in the root directory with the following:

MONGO_URI="your mongodb project's database url"
MONGO_DB = "mongodb database name"
MONGO_COLLECTION = "mongodb database table or collecction name"

---

### 2. 🐍 Install Dependencies

pip install -r requirements.txt

---

### 3. ▶️ Run the App Locally

streamlit run app.py

## 📤 MongoDB Integration

The app saves each prediction in MongoDB Atlas.

---

## ✨ Future Improvements

- Visualize prediction statistics
- Model monitoring dashboard
- Deploy to cloud (AWS, GCP, Heroku, etc.)

---

## 🙌 Acknowledgements

This project is part of an end-to-end data science portfolio showcasing ML deployment, data engineering, and UI development.

---

## 📫 Contact

**Author**: Shushil Shah  
**LinkedIn**: htpps://linkedin.com/in/shushilshah
