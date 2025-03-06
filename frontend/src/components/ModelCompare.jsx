import { BarChart, Bar, XAxis, YAxis, CartesianGrid } from 'recharts';

const ModelComparison = ({ models }) => (
  <div className="model-comparison">
    <BarChart width={800} height={400} data={models}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />
      <YAxis />
      <Bar dataKey="accuracy" fill="#8884d8" />
      <Bar dataKey="f1_score" fill="#82ca9d" />
    </BarChart>
    
    <table className="academic-table">
      <thead>
        <tr>
          <th>Model</th>
          <th>Accuracy</th>
          <th>F1 Score</th>
          <th>Inference Time</th>
        </tr>
      </thead>
      <tbody>
        {models.map(model => (
          <tr key={model.name}>
            <td>{model.name}</td>
            <td>{model.accuracy}%</td>
            <td>{model.f1_score}</td>
            <td>{model.inference_time}ms</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);