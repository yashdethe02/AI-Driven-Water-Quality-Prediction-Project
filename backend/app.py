from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained model
with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Perform prediction using the model
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)