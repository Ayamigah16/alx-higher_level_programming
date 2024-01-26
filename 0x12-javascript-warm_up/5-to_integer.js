#!/usr/bin/node

// Check if the first argument can be converted to an integer
const num = parseInt(process.argv[2]);

// Use console.log(...) to print the result based on the conversion
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
