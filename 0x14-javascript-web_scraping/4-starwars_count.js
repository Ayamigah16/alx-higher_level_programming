#!/usr/bin/node

'use strict';

const request = require('request');

// Get the API URL of the Star Wars API from command line arguments
const apiUrl = process.argv[2];

// Character ID of Wedge Antilles
const characterId = 18;

// Make a GET request to the API endpoint
request.get(apiUrl, (error, response, body) => {
  // If an error occurred during the request, print the error object
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const filmsData = JSON.parse(body).results;

  // Filter the films where Wedge Antilles is present
  const filmsWithWedge = filmsData.filter(film =>
    film.characters.includes(`${apiUrl}${characterId}/`)
  );

  // Print the number of films where Wedge Antilles is present
  console.log(filmsWithWedge.length);
});
