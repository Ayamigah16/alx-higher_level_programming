#!/usr/bin/node

// Define the function add that returns the addition of two integers
function add (a, b) {
  return a + b;
}

// Export the add function to make it visible from outside
module.exports = {
  add
};
