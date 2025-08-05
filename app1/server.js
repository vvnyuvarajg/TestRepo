const express = require('express');
const path = require('path');
const app = express();
const port = process.env.PORT || 4001; // Use port 4001, or a port defined by environment variable

// Serve static files from the current directory (where index.html is)
app.use(express.static(__dirname));

// Define a route for the root URL
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Start the server
app.listen(port, () => {
  console.log(`Good Afternoon listening at http://localhost:${port}`);
});
