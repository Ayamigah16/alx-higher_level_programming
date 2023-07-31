#!/usr/bin/python3
"""
Defines the Base Class
"""
import json
import csv
import turtle


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the Base class.

        Args:
            id (int): An integer representing the
        object's id. If None, a new id is assigned
        based on the class attribute __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation
        of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string.

        Args:
            json_string (str): A JSON string
        representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            **dictionary (dict): The dictionary containing
        the attributes.

        Returns:
            Base: An instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = None

        if dummy_instance:
            dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a file.

        Args:
            list_objs (list): A list of instances to save.
        """
        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**data) for data in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of objects to a CSV file.

        Args:
        list_objs (list): List of instances to be saved to the CSV file.

        Returns:
        None
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding='utf-8') as f:
            for obj in list_objs:
                f.write(obj.to_csv_row() + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """Loads objects from a CSV file and returns a
        list of instances of the class.

        Returns:
        list: List of instances loaded from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                return [cls.from_csv_row(row.strip()) for row in f]
        except FileNotFoundError:
            return []

    def to_csv_row(self):
        """Convert instance attributes to a CSV row.

        Returns:
            list: The CSV row representing the instance attributes.
        """
        raise NotImplementedError(
            "to_csv_row method must be implemented in subclasses")

    @classmethod
    def from_csv_row(cls, row):
        """Convert a CSV row to a dictionary of attributes.

        Args:
            row (list): The CSV row representing the instance attributes.

        Returns:
            dict: A dictionary containing the instance attributes.
        """
        raise NotImplementedError(
            "from_csv_row method must be implemented in subclasses")

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the Turtle graphics module.

        Args:
            list_rectangles (list): A list of Rectangle instances to draw.
            list_squares (list): A list of Square instances to draw.
        """
        screen = turtle.Screen()
        screen.setup(800, 600)
        screen.bgcolor("white")

        pen = turtle.Turtle()
        pen.speed(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        screen.mainloop()
