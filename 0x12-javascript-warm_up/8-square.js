#!/usr/bin/node

// Check if the first argument is provided and can be converted to a positive integer
const size = parseInt(process.argv[2]);

// Check if size is a valid positive integer
if (!isNaN(size) && size > 0) {
  // Loop through and use console.log(...) to print a square of size x size
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  // If no or invalid argument is provided, print "Missing size"
  console.log('Missing size');
}
