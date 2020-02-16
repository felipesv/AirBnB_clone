#!/usr/bin/python3
"""
defines all common attributes/methods for other classes
"""
import datetime
import models
import uuid


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    datefmt = '%Y-%m-%dT%H:%M:%S.%f'
                    value = datetime.datetime.strptime(value, datefmt)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str method"""
        msg = "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                    self.__dict__)
        return msg

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        cr_at = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        up_at = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        new_dict['created_at'] = cr_at
        new_dict['updated_at'] = up_at
        return new_dict
