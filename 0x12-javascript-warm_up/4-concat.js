#!/usr/bin/node

// Check if at least two arguments are passed
if (process.argv[2] && process.argv[3]) {
  // Use console.log(...) to print the concatenated string
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
} else {
  // If fewer than two arguments are passed, print "undefined is undefined"
  console.log('undefined is undefined');
}
