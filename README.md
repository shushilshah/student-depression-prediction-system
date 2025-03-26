# Student Depression Prediction App

## Introduction

Mental health issues among students have become a growing concern in recent years. With academic pressure, career uncertainty, and lifestyle challenges, students are increasingly vulnerable to stress, anxiety, and depression.

This project — Student Depression Prediction App — aims to leverage the power of Machine Learning to predict whether a student is likely to suffer from depression based on their demographic, academic, and lifestyle information.

The goal is to build a simple yet impactful tool that can assist educators, counselors, and health professionals in early detection and preventive care. This is not a diagnostic tool, but a data-driven support system to raise awareness and prompt further conversation.

This project includes:

- An end-to-end **ML pipeline** (training & transformation)
- **MongoDB Atlas** integration to store predictions.
- **Streamlit** UI application to take user input.

---

## Features

- User-friendly form for input
- Predicts if a person is likely depressed or not
- Saves prediction history in MongoDB
- Dynamic model training feature.

---

## Tech Stack

- **Python**
- **Scikit-learn**, **Pandas**, **Joblib**
- **Streamlit**
- **MongoDB Atlas** (Cloud Database)

---

## Setup Instructions

### 1. Environment Setup

Create a `.env` file in the root directory with the following:

MONGO_URI="your mongodb project's database url"
MONGO_DB = "mongodb database name"
MONGO_COLLECTION = "mongodb database table or collecction name"

---

### 2. Install Dependencies

pip install -r requirements.txt

---

### 3. Run the App Locally

streamlit run app.py

## MongoDB Integration

Fetch the whole data for training from database for each user input so it is dynamic.
The app saves each prediction in MongoDB Atlas.

---

## Future Improvements

- Visualize prediction statistics
- Model monitoring dashboard
- Deploy to cloud (AWS, GCP, Heroku, etc.)

---

## Acknowledgements

This project is part of an end-to-end data science portfolio showcasing ML deployment, data engineering, and UI development.

---

## Contact

**Author**: Shushil Shah  
**LinkedIn**: htpps://linkedin.com/in/shushilshah
