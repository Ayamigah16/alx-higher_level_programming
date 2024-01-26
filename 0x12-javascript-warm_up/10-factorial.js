#!/usr/bin/node

// Define a recursive function factorial
function factorial (n) {
  if (isNaN(n) || n < 0) {
    // Factorial of NaN or negative numbers is 1
    return 1;
  } else if (n === 0) {
    // Factorial of 0 is 1
    return 1;
  } else {
    // Compute the factorial recursively
    return n * factorial(n - 1);
  }
}

// Check if the first argument is provided
if (process.argv[2]) {
  // Convert the argument to an integer and call the factorial function
  const result = factorial(parseInt(process.argv[2]));

  // Use console.log(...) to print the result
  console.log(result);
} else {
  // If the argument is missing, print 1
  console.log(1);
}
