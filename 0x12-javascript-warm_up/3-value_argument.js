#!/usr/bin/node

// Check if there is at least one argument
if (process.argv[2]) {
  // Use console.log(...) to print the first argument
  console.log(process.argv[2]);
} else {
  // If no arguments are passed, print "No argument"
  console.log('No argument');
}
