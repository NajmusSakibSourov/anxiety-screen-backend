import functions_framework
from flask import jsonify
import numpy as np

# For the MVP, we are using a logic-based approach which mimics the ML model's decision boundary.
# In the future, we can load a .pkl model here using joblib.

@functions_framework.http
def predict_anxiety(request):
    """
    HTTP Cloud Function that accepts a JSON request with GAD-7 scores and response time.
    Returns a JSON response with the anxiety classification.
    """
    
    # Handle CORS (Cross-Origin Resource Sharing) for browser requests
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    request_json = request.get_json(silent=True)
    
    if not request_json:
        return (jsonify({"error": "Invalid JSON"}), 400, headers)

    try:
        # Extract GAD-7 scores (expected keys: q1, q2, q3, q4, q5, q6, q7)
        # Each score should be between 0 and 3
        scores = []
        for i in range(1, 8):
            key = f'q{i}'
            if key not in request_json:
                return (jsonify({"error": f"Missing field: {key}"}), 400, headers)
            scores.append(int(request_json[key]))

        # Calculate total GAD-7 score
        total_score = sum(scores)
        
        # Classification Logic (Standard GAD-7 thresholds)
        # 0-4: Minimal -> Low
        # 5-9: Mild -> Low
        # 10-14: Moderate -> Moderate
        # 15-21: Severe -> High
        
        classification = "Low"
        if total_score >= 15:
            classification = "High"
        elif total_score >= 10:
            classification = "Moderate"
        
        # Log response time for research purposes (if provided)
        response_time = request_json.get('response_time', 'N/A')
        print(f"Processed request. Score: {total_score}, Class: {classification}, Time: {response_time}")

        return (jsonify({
            "score": total_score,
            "classification": classification
        }), 200, headers)

    except Exception as e:
        return (jsonify({"error": str(e)}), 500, headers)
