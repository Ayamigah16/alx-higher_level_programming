// 5-square.js

const Rectangle = require('./4-rectangle'); // Import the Rectangle class

class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of the parent class (Rectangle)
    super(size, size);
  }
}

module.exports = Square;
