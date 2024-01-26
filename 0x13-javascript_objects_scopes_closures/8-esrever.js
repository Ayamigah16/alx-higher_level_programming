// 8-esrever.js

exports.esrever = function (list) {
  // Clone the list to avoid modifying the original array
  const reversedList = [...list];

  // Swap elements from the beginning and end
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    const temp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = temp;
  }

  return reversedList;
};
