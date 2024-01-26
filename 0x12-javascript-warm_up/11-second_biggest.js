#!/usr/bin/node

// Check if there are at least two arguments
if (process.argv.length < 4) {
  // If no or only one argument is provided, print 0
  console.log(0);
} else {
  // Convert all arguments to integers and sort them in descending order
  const numbers = process.argv.slice(2).map(Number).sort((a, b) => b - a);

  // Print the second element (second biggest) in the sorted array
  console.log(numbers[1]);
}
