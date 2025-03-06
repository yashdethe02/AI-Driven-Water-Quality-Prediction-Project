import React, { useState } from 'react';
import { TextField, Button, Paper } from '@mui/material';

const ChatPanel = ({ onQuestionSubmit }) => {
  const [query, setQuery] = useState('');
  
  return (
    <Paper elevation={3} style={{ padding: '20px', marginTop: '20px' }}>
      <TextField
        fullWidth
        label="Ask about water quality"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <Button 
        variant="contained" 
        color="primary" 
        style={{ marginTop: '10px' }}
        onClick={() => onQuestionSubmit(query)}
      >
        Ask AI
      </Button>
    </Paper>
  );
};