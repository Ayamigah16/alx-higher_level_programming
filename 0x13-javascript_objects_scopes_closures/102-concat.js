// 102-concat.js

const fs = require('fs');

// Get the file paths from command line arguments
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

// Read the content of the first source file
const content1 = fs.readFileSync(sourceFile1, 'utf-8');

// Read the content of the second source file
const content2 = fs.readFileSync(sourceFile2, 'utf-8');

// Concatenate the contents of the two files
const concatenatedContent = content1 + content2;

// Write the concatenated content to the destination file
fs.writeFileSync(destinationFile, concatenatedContent);

console.log(`Concatenation complete. Result saved to ${destinationFile}`);
