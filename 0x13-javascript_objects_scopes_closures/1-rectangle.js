// 1-rectangle.js

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = (h !== undefined) ? h : undefined;
  }
}

module.exports = Rectangle;
