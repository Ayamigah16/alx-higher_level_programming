// 7-occurrences.js

exports.nbOccurences = function (list, searchElement) {
  // Use the reduce function to count occurrences
  const occurrences = list.reduce((count, element) => {
    return (element === searchElement) ? count + 1 : count;
  }, 0);

  return occurrences;
};
