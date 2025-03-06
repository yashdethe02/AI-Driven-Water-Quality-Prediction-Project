import React from 'react';
import { Box, Grid, Typography } from '@mui/material';
import { LineChart, Line, ResponsiveContainer } from 'recharts';

const Dashboard = ({ metrics }) => (
  <Box sx={{ p: 3 }}>
    <Grid container spacing={3}>
      <Grid item xs={12} md={6}>
        <Box sx={{ bgcolor: 'background.paper', p: 2, borderRadius: 2 }}>
          <Typography variant="h6" gutterBottom>Water Quality Trends</Typography>
          <div style={{ height: 300 }}>
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={metrics}>
                <Line type="monotone" dataKey="ph" stroke="#8884d8" />
                <Line type="monotone" dataKey="turbidity" stroke="#82ca9d" />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </Box>
      </Grid>
      
      <Grid item xs={12} md={6}>
        <Box sx={{ 
          bgcolor: 'background.paper', 
          p: 2, 
          borderRadius: 2,
          height: '100%',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center'
        }}>
          <Typography variant="h6" gutterBottom>Key Metrics</Typography>
          <Box sx={{ display: 'flex', justifyContent: 'space-around' }}>
            <MetricBox title="pH Level" value={metrics.ph} idealRange="6.5-8.5" />
            <MetricBox title="Turbidity" value={metrics.turbidity} unit="NTU" />
          </Box>
        </Box>
      </Grid>
    </Grid>
  </Box>
);