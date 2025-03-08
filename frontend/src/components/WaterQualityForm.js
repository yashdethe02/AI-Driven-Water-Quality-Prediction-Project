import React, { useState } from 'react';

function WaterQualityForm() {
  const [features, setFeatures] = useState({});
  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setFeatures({ ...features, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ features: Object.values(features) })
    });
    const data = await response.json();
    setPrediction(data.prediction);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Feature 1:
        <input type="text" name="feature1" onChange={handleChange} />
      </label>
      <label>
        Feature 2:
        <input type="text" name="feature2" onChange={handleChange} />
      </label>
      {/* Add more feature inputs as needed */}
      <button type="submit">Predict</button>
      {prediction && <p>Prediction: {prediction}</p>}
    </form>
  );
}

export default WaterQualityForm;