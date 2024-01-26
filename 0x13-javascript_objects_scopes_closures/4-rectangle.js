// 4-rectangle.js

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

  rotate () {
    // Exchange width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Double the width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
