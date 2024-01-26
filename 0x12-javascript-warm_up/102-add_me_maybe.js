#!/usr/bin/node

// Define the function addMeMaybe that increments and calls a given function
function addMeMaybe (number, theFunction) {
  // Increment the given number
  number++;

  // Call the given function with the incremented number
  theFunction(number);
}

// Export the addMeMaybe function to make it visible from outside
module.exports = {
  addMeMaybe
};
