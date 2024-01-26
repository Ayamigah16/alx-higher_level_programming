#!/usr/bin/node

// Check if the first argument is provided and can be converted to an integer
const occurrences = parseInt(process.argv[2]);

// Check if occurrences is a valid positive integer
if (!isNaN(occurrences) && occurrences > 0) {
  // Loop through and use console.log(...) to print "C is fun" x times
  for (let i = 0; i < occurrences; i++) {
    console.log('C is fun');
  }
} else {
  // If no or invalid argument is provided, print "Missing number of occurrences"
  console.log('Missing number of occurrences');
}
