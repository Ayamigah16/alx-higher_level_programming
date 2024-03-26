#!/usr/bin/node

'use strict';

const fs = require('fs');

// Get the file path and string to write from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, content, 'utf-8', (error) => {
  // If an error occurred during writing, print the error object
  if (error) {
    console.error(error);
    return;
  }

  console.log(`Content has been written to ${filePath}`);
});
