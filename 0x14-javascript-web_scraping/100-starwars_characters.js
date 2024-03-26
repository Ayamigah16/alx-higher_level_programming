#!/usr/bin/node

'use strict';

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// URL of the Star Wars API endpoint
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

  // Array to store character names
  const characterNames = [];

  // Fetch details of each character in the movie
  const fetchCharacters = async () => {
    for (const characterUrl of movieData.characters) {
      try {
        const characterResponse = await new Promise((resolve, reject) => {
          request.get(characterUrl, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              resolve(body);
            }
          });
        });
        const characterData = JSON.parse(characterResponse);
        characterNames.push(characterData.name);
      } catch (error) {
        console.error(error);
      }
    }
    // Print the character names
    characterNames.forEach(name => console.log(name));
  };

  fetchCharacters();
});
