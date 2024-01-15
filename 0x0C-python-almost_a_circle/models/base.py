#!/usr/bin/python3
"""Contains a class Bass with a functin for managing id attributes"""
import json
import csv


class Base:
    """
    The Base class works as a base for managing id attributes in other classes.

    Attributes:
        __nb_objects (int): A private class attribute,
        check number of instances created.
        id (int): A public instance attribute,
        represent unique id for each instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): If provided, assign provided ID to the instance. Else,
                generate new ID based on the current value of __nb_objects.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            JSON string representation of the list of dictionaries.
        """
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            cls: The class.
            list_objs (list): A list of instances that inherit from Base.

        Returns:
            None
        """
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w") as file:
            obj_dicts = [obj.to_dictionary() if hasattr(obj, 'to_dictionary')
                         else obj for obj in list_objs or []]
            json.dump(obj_dicts, file)

    def to_dictionary(self):
        return {"id": self.id}

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            instance: An instance of the class with attributes set.
        """
        new = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        for key, value in dictionary.items():
            if key == "id":
                setattr(new, key, value)
            else:
                setattr(new, key, value)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a file.

        Returns:
            list: A list of instances.
        """
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r") as file:
                first_char = file.read(1)
                if first_char:
                    file.seek(0)
                    dict_list = json.load(file)
                    return [cls.create(**item) for item in dict_list]
                else:
                    return []
        except FileNotFoundError:
            return []

    def update(self, *args, **kwargs):
        if args:
            attributes = ["id"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV representation of list_objs to a file.

        Args:
            cls: The class.
            list_objs (list): A list of instances that inherit from Base.

        Returns:
            None
        """
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs or []:
                row_data = list(obj.to_dictionary().values())
                writer.writerow(row_data)

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances loaded from a CSV file.

        Returns:
            list: A list of instances.
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                csv_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_of_dicts = []
                for row in csv_reader:
                    new_dict = {}
                    for key, value in row.items():
                        if isinstance(value, list) and len(value) == 1:
                            value = value[0]
                        try:
                            new_dict[key] = int(value)
                        except ValueError:
                            new_dict[key] = value
                    list_of_dicts.append(new_dict)

                list_of_instances = ([cls.create(**{str(k): v for k, v
                                                    in obj_dict.items()})
                                      for obj_dict in list_of_dicts])

                return list_of_instances
        except IOError:
            return []

    @classmethod
    def convert_value(cls, value):
        """Convert the value from CSV to the appropriate type."""
        return int(value) if value.isdigit() else value
