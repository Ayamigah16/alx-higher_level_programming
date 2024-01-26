// 101-sorted.js

const dict = require('./101-data').dict;

// Initialize the new dictionary
const sortedDict = {};

// Iterate over the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // If the occurrences is not a key in sortedDict, create an array for it
  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }

  // Push the user id to the corresponding occurrences key
  sortedDict[occurrences].push(userId);
}

console.log(sortedDict);
