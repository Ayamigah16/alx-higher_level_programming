#!/usr/bin/node

'use strict';

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// URL of the Star Wars API endpoint for the movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API endpoint
request.get(apiUrl, (error, response, body) => {
  // If an error occurred during the request, print the error object
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const movieData = JSON.parse(body);

  // Function to fetch characters in order
  const fetchCharactersInOrder = async () => {
    // Iterate over the characters array in the movie data
    for (const characterUrl of movieData.characters) {
      try {
        // Make a GET request to fetch character details
        const characterResponse = await new Promise((resolve, reject) => {
          request.get(characterUrl, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              resolve(body);
            }
          });
        });
        // Parse the character response JSON
        const characterData = JSON.parse(characterResponse);
        // Print the character name
        console.log(characterData.name);
      } catch (error) {
        console.error(error);
      }
    }
  };

  // Call the function to fetch characters in order
  fetchCharactersInOrder();
});
