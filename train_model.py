import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# 1. Generate Synthetic Data (if not exists)
DATA_FILE = 'survey_data.csv'
MODEL_FILE = 'anxiety_model.pkl'

def generate_data(n_samples=1000):
    print(f"Generating {n_samples} synthetic samples...")
    np.random.seed(42)
    
    # Feature Groups
    # Demographic
    age = np.random.randint(13, 19, n_samples)
    gender = np.random.choice([0, 1], n_samples) # 0: Male, 1: Female
    
    # Academic Stress (1-5 scale)
    gpa = np.round(np.random.uniform(2.0, 5.0, n_samples), 2)
    exam_pressure = np.random.randint(1, 6, n_samples)
    homework_load = np.random.randint(1, 6, n_samples)
    study_hours = np.random.randint(1, 10, n_samples)
    
    # Psychometric (GAD-7 style questions 0-3)
    # We will simulate that higher stress leads to higher anxiety scores
    nervousness = np.random.randint(0, 4, n_samples)
    worry = np.random.randint(0, 4, n_samples)
    restlessness = np.random.randint(0, 4, n_samples)
    trouble_relaxing = np.random.randint(0, 4, n_samples)
    fear = np.random.randint(0, 4, n_samples)
    physical_symptoms = np.random.randint(0, 4, n_samples)
    sleep_disturbance = np.random.randint(0, 4, n_samples)
    
    # Lifestyle
    sleep_duration = np.random.randint(4, 10, n_samples)
    screen_time = np.random.randint(1, 12, n_samples)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Age': age,
        'Gender': gender,
        'GPA': gpa,
        'Exam_Pressure': exam_pressure,
        'Homework_Load': homework_load,
        'Study_Hours': study_hours,
        'Nervousness': nervousness,
        'Worry': worry,
        'Restlessness': restlessness,
        'Trouble_Relaxing': trouble_relaxing,
        'Fear': fear,
        'Physical_Symptoms': physical_symptoms,
        'Sleep_Disturbance': sleep_disturbance,
        'Sleep_Duration': sleep_duration,
        'Screen_Time': screen_time
    })
    
    # Calculate a "True" Anxiety Score for labeling (Weighted sum)
    # This is just to create a somewhat realistic relationship for the model to learn
    anxiety_score = (
        (df['Nervousness'] + df['Worry'] + df['Restlessness'] + df['Trouble_Relaxing'] + 
         df['Fear'] + df['Physical_Symptoms'] + df['Sleep_Disturbance']) * 1.5 +
        (df['Exam_Pressure'] + df['Homework_Load']) * 1.0 -
        (df['Sleep_Duration'] * 0.5)
    )
    
    # Define Classes based on score
    # Thresholds are arbitrary for this synthetic generation to ensure balanced classes
    conditions = [
        (anxiety_score < 15),
        (anxiety_score >= 15) & (anxiety_score < 25),
        (anxiety_score >= 25)
    ]
    choices = ['Low', 'Moderate', 'High']
    df['Anxiety_Level'] = np.select(conditions, choices)
    
    return df

def train():
    if not os.path.exists(DATA_FILE):
        df = generate_data()
        try:
            df.to_csv(DATA_FILE, index=False)
            print(f"Saved data to {DATA_FILE}")
        except OSError:
            print("Read-only file system. Skipping CSV save.")
    else:
        print(f"Loading data from {DATA_FILE}")
        df = pd.read_csv(DATA_FILE)
        
    print("Data Head:")
    print(df.head())
    
    # Preprocessing
    X = df.drop('Anxiety_Level', axis=1)
    y = df['Anxiety_Level']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train
    print("Training Random Forest Classifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluate
    y_pred = clf.predict(X_test)
    print("Model Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    # Save Model
    try:
        joblib.dump(clf, MODEL_FILE)
        print(f"Model saved to {MODEL_FILE}")
    except OSError:
        print("Read-only file system detected. Skipping model save.")
    
    return clf

def get_trained_model():
    return train()

if __name__ == "__main__":
    train()
