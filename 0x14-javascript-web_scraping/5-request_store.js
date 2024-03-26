#!/usr/bin/node

'use strict';

const fs = require('fs');
const request = require('request');

// Get the URL to request and file path to
// store the response from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request.get(url, (error, response, body) => {
  // If an error occurred during the request, print the error object
  if (error) {
    console.error(error);
    return;
  }

  // Write the body response to the file
  fs.writeFile(filePath, body, 'utf-8', (error) => {
    // If an error occurred during writing, print the error object
    if (error) {
      console.error(error);
      return;
    }
    console.log(`Response body has been stored in ${filePath}`);
  });
});
