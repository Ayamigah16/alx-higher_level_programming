#!/usr/bin/node

'use strict';

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API endpoint
request.get(apiUrl, (error, response, body) => {
    // If an error occurred during the request,
    // print the error object
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const todos = JSON.parse(body);

  // Object to store the number of completed tasks per user ID
  const completedTasks = {};

  // Iterate through the todos
  todos.forEach(todo => {
    // Check if the task is completed
    if (todo.completed) {
	// If the user ID doesn't exist in the completedTasks
	// object, initialize it with count 1
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 1;
      } else {
          // Otherwise, increment the count of completed
	  // tasks for that user ID
        completedTasks[todo.userId]++;
      }
    }
  });

  // Print the number of completed tasks per user ID
  console.log(completedTasks);
});
