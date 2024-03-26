#!/usr/bin/node

'use strict';

const request = require('request');

// Get the URL to request from command line arguments
const url = process.argv[2];

// Make a GET request to the URL
request.get(url, (error, response) => {
  // If an error occurred during the request, print the error object
  if (error) {
    console.error(error);
    return;
  }

  // Print the status code
  console.log(`code: ${response.statusCode}`);
});
