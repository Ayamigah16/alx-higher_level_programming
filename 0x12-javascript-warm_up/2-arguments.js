#!/usr/bin/node

// Check the number of arguments passed
const argsCount = process.argv.length;

// Use console.log(...) to print a message based on the number of arguments
if (argsCount === 2) {
  console.log('No argument');
} else if (argsCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
