import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import joblib
import os
import numpy as np

# Load necessary models
stop_words = set(stopwords.words('english'))
tfidf_vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
kmeans_model = joblib.load("models/kmeans_model.pkl")

def preprocess_text(text):
    text = str(text).lower()
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_tokens)

# Define categories dynamically
categories = {
    0: "Data Science and Machine Learning",
    1: "Game Development",
    2: "Java Programming and Web Applications",
    3: "General Programming and Software Development",
    4: "Databases and SQL Administration",
    5: "Microsoft Technologies (Windows, Office, SharePoint)",
    6: "Networking and Cybersecurity",
    7: "Certification and Exam Preparation",
    8: "Mobile App Development (Android & iOS)",
    9: "Web Development (HTML, CSS, JavaScript)"
}

def categorizeBooks(bookdescription):
    # Clean the input text
    bookdescription_cleaned = preprocess_text(bookdescription)

    # Convert to TF-IDF features
    bookdescription_vectorized = tfidf_vectorizer.transform([bookdescription_cleaned])

    # Predict the primary category
    predicted_cluster = kmeans_model.predict(bookdescription_vectorized)[0]

    # Get distances to all clusters
    distances = kmeans_model.transform(bookdescription_vectorized)[0]

    # Identify the top 3 most related clusters
    closest_clusters = np.argsort(distances)[:3]

    # Assign category labels
    main_category = categories.get(closest_clusters[0], "Unknown")
    related_topics = [categories.get(closest_clusters[i], "Unknown") for i in range(1, 3)]

    return main_category, related_topics
