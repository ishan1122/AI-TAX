from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load trained AI model
model = joblib.load("fraud_detection_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        prediction = model.predict([[data['amount_log'], data['transaction_type'], data['account_balance']]])
        return jsonify({"fraud_detected": bool(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
