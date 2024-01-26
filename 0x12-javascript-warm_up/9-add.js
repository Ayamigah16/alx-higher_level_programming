#!/usr/bin/node

// Define a function add with the prototype function add(a, b)
function add (a, b) {
  return a + b;
}

// Check if both arguments are provided
if (process.argv[2] && process.argv[3]) {
  // Convert arguments to integers and call the add function
  const result = add(parseInt(process.argv[2]), parseInt(process.argv[3]));

  // Use console.log(...) to print the result
  console.log(result);
} else {
  // If one or both arguments are missing, print NaN
  console.log('NaN');
}
