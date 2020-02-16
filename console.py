#!/usr/bin/python3
'''create a console'''
import cmd
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        '''EOF command to exit the program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        '''Empty line'''
        return ""

    def do_create(self, line):
        '''Create commands'''
        if not line:
                print("** class name missing **")
                return

        listClass = ["BaseModel", "User", "Place", "State", "City", "Amenity"]
        data = line.split(" ")
        nameClass = data[0]

        if line in listClass:
                newBM = eval(nameClass)()
                print(newBM.id)
        else:
                print("** class doesn't exist **")

    def do_show(self, line):
        '''show commands'''
        if not line:
            print("** class name missing **")
            return

        listClass = ["BaseModel", "User", "Place", "State", "City", "Amenity"]
        data = line.split(" ")
        nameClass = data[0]

        if nameClass in listClass:
            if len(data) == 1:
                print("** instance id missing **")
                return

            try:
                idObject = "{}.{}".format(data[0], data[1])
                dictObj = storage.all()
                print(dictObj[idObject])
            except:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        '''destroy command'''
        if not line:
            print("** class name missing **")
            return

        listClass = ["BaseModel", "User", "Place", "State", "City", "Amenity"]
        data = line.split(" ")
        nameClass = data[0]

        if nameClass in listClass:
            if len(data) == 1:
                print("** instance id missing **")
                return

            try:
                idObject = "{}.{}".format(data[0], data[1])
                dictObj = storage.all()
                del dictObj[idObject]
                storage.save()
            except:
                print("** no instance found ** ")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        '''all command'''
        dictObj = storage.all()

        if not line:
            newList = []
            for value in dictObj.values():
                    newList.append(str(value))
            print(newList)
        else:
            data = line.split(" ")
            newList = []
            for value in dictObj.values():
                if(value.__class__.__name__ == data[0]):
                    newList.append(str(value))
            print(newList)

    def do_update(self, line):
        if not line:
            print("** class name missing **")
            return

        listClass = ["BaseModel", "User", "Place", "State", "City", "Amenity"]
        data = line.split(" ")
        dictObj = storage.all()

        if data[0] not in listClass:
            print("** class doesn't exist **")
        if len(data) < 2:
            print("** instance id missing **")

        try:
            obj = dictObj["{}.{}".format(data[0], data[1])]
        except:
            print("** no instance found **")

        if len(data) < 3:
            print("** attribute name missing **")
        if len(data) < 4:
            print("** value missing **")

        setattr(obj, data[3], data[4])
        setattr(obj, "updated_at", datetime.now())
        storage.save()

if __name__ == "__main__":
        HBNBCommand().cmdloop()
