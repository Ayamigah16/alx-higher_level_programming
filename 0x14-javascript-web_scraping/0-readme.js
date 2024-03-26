#!/usr/bin/node

'use strict';

const fs = require('fs');

// Get the file path from command line arguments
const filePath = process.argv[2];

// Read the content of the file
fs.readFile(filePath, 'utf-8', (error, data) => {
  // If an error occurred during reading, print the error object
  if (error) {
    console.error(error);
    return;
  }

  // Print the content of the file
  console.log(data);
});
