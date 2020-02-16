#!/usr/bin/python3
"""
serializes instances to JSON and deserializes JSON to instances
"""
import json
from models.base_model import BaseModel



class FileStorage:
    """
    serializes instances to JSON and deserializes JSON to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """constructor"""

    def all(self):
        """returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name = obj.__class__.__name__
        noid = obj.id
        key = "{}.{}".format(name, noid)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()

        namefile = FileStorage.__file_path
        with open(namefile, mode="w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        namefile = self.__file_path
        try:
            with open(namefile, encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    nameClass = value["__class__"]
                    newobj = eval(nameClass)(**value)
                    FileStorage.__objects[key] = newobj
        except Exception:
            pass
