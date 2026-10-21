from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows your GitHub Pages frontend to talk to this backend

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "EcoTrace Python Backend is running successfully!"})

@app.route('/api/calculate', methods=['POST'])
def calculate_footprint():
    data = request.get_json() or {}
    
    electricity_kwh = float(data.get('electricity_kwh', 0))
    waste_kg = float(data.get('waste_kg', 0))
    
    carbon_electricity = electricity_kwh * 0.82
    carbon_waste = waste_kg * 0.5
    total_carbon = round(carbon_electricity + carbon_waste, 2)
    
    return jsonify({
        "status": "success",
        "total_carbon_kg": total_carbon,
        "message": "Calculation processed by Python backend!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)