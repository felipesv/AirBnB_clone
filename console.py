#!/usr/bin/python3
'''create a console'''
import cmd
import shlex
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        '''EOF command to exit the program'''
        print("")
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

        listClass = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                     "Review"]
        data = line.split(" ")
        nameClass = data[0]

        if line in listClass:
                newBM = eval(nameClass)()
                newBM.save()
                print(newBM.id)
        else:
                print("** class doesn't exist **")

    def do_show(self, line):
        '''show commands'''
        if not line:
            print("** class name missing **")
            return

        listClass = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                     "Review"]
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

        listClass = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                     "Review"]
        data = line.split(" ")
        nameClass = data[0]

        if nameClass in listClass:
            if len(data) == 1:
                print("** instance id missing **")
                return

            idObject = "{}.{}".format(data[0], data[1])
            dictObj = storage.all()
            if idObject in dictObj:
                del dictObj[idObject]
                storage.save()
                return
            print("** no instance found ** ")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        '''all command'''
        dictObj = storage.all()
        listClass = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                     "Review"]
        if not line:
            newList = []
            for value in dictObj.values():
                    newList.append(str(value))
            print(newList)
        else:

            data = line.split(" ")
            if data[0] not in listClass:
                print("** class doesn't exist **")
                return
            newList = []
            for value in dictObj.values():
                if(value.__class__.__name__ == data[0]):
                    newList.append(str(value))
            print(newList)

    def do_update(self, line):
        '''update command'''
        if not line:
            print("** class name missing **")
            return

        listClass = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                     "Review"]
        data = shlex.split(line)
        dictObj = storage.all()

        if len(data) == 0 or data[0] not in listClass:
            print("** class doesn't exist **")
            return
        if len(data) == 1:
            print("** instance id missing **")
            return

        try:
            obj = dictObj["{}.{}".format(data[0], data[1])]
        except:
            print("** no instance found **")
            return

        if len(data) == 2:
            print("** attribute name missing **")
            return
        if len(data) == 3:
            print("** value missing **")
            return

        setattr(obj, data[2], data[3])
        setattr(obj, "updated_at", datetime.now())
        storage.save()

    def do_count(self, line):
        '''count command'''
        if not line:
            print("** class name missing **")
            return

        listClass = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                     "Review"]
        if line in listClass:
            objcDic = storage.all()
            count = 0
            for values in objcDic.values():
                if values.__class__.__name__ == line:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        '''others commands'''
        data = line.split(".")
        if len(data) < 2:
            return
        listFn = ["all()", "count()"]
        if data[1] in listFn:
            cmdString = "{}".format(data[0])
            if data[1] == listFn[0]:
                self.do_all(cmdString)
            elif data[1] == listFn[1]:
                self.do_count(cmdString)
        else:
            data = data[1].split("(")
            listFn = ["show", "update"]
            if data[0] in listFn:
                data[1] = data[1][:-1]
                if len(data[1]) > 2:
                    print("care chimba")
                else:
                    print("care chimba 2")
                # if data[0] == listFn[0]:
            else:
                print("** command doesn't exist **")


if __name__ == "__main__":
        HBNBCommand().cmdloop()
