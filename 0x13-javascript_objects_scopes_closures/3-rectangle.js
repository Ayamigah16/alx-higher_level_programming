// 3-rectangle.js

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object
      Object.create(null);
    }
  }

  print () {
    // Check if width and height are defined
    if (this.width !== undefined && this.height !== undefined) {
      // Loop to print the rectangle using 'X'
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
