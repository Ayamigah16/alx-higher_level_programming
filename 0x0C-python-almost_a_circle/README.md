# 0x0C. Python - Almost a circle
### General
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Takss
1. ***Base class:*** Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package. Create a file named models/base.py:

2. ***First Rectangle:***Write the class Rectangle that inherits from Base

3. ***Validate attributes:*** Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

4. ***Area first:*** Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

5. *** Display #0:*** Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.

6. *** __str__:*** Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

7. ***Display #1:***Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

8. ***Update #0:*** Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:

- 1st argument should be the id attribute
- 2nd argument should be the width attribute
- 3rd argument should be the height attribute
- 4th argument should be the x attribute
- 5th argument should be the y attribute

9. ***And now, the Square!*** Write the class Square that inherits from Rectangle:

10. ***Square size:***Update the class Square by adding the public getter and setter size
