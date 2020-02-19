# AirBnB clone
Airbnb is an online marketplace that connects people who want to rent out their homes with people who are looking for accommodations in that locale. ... For hosts, participating in Airbnb is a way to earn some income from their property, but with the risk that the guest might do damage to it.

# Objectives

 - How to create a Python package
 - How to create a command interpreter in Python using the cmd module
 - What is Unit testing and how to implement it in a large project
 - How to serialize and deserialize a Class
 - How to write and read a JSON file
 - How to manage datetime
 - What is an UUID
 - What is *args and how to use it
 - What is **kwargs and how to use it
 - How to handle named arguments in a function

# Requirements
### Python Scripts
 - Allowed editors: vi, vim, emacs
 - All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
 - All your files should end with a new line
 - The first line of all your files should be exactly #!/usr/bin/python3
 - A README.md file, at the root of the folder of the project, is mandatory
 - Your code should use the PEP 8 style (version 1.7 or more)
 - All your files must be executable
 - The length of your files will be tested using wc
 - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
 - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
 - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

### Python Unit Tests

 - Allowed editors: vi, vim, emacs
 - All your files should end with a new line
 - All your test files should be inside a folder tests
 - You have to use the unittest module
 - All your test files should be python files (extension: .py)
 - All your test files and folders should start by test_
 - Your file organization in the tests folder should be the same as your project
 - e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
 - e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
 - All your tests should be executed by using this command: python3 -m unittest discover tests
 - You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
 - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
 - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
 - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
 - We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# Execution
But also in non-interactive mode: (like the Shell project in C)
> $ echo "help" | ./console.py
> (hbnb)
> Documented commands (type help <topic>):
> EOF  help  quit

> (hbnb) 
> $
> cat test_help
> help
> $

> $ cat test_help | ./console.py
> (hbnb)
> Documented commands (type help <topic>):
> EOF  help  quit
> (hbnb) 
> $

# Tasks

### 0. README, AUTHORS 
Write a README.md with description of the project and description of the command interpreter.
AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository.
### 1. Be PEP8 compliant!
Write beautiful code that passes the PEP8 checks.
### 2. Unittests
All your files, classes, functions must be tested with unit tests
### 3. BaseModel
Write a class BaseModel that defines all common attributes/methods for other classes
### 4. Create BaseModel from dictionary
Previously we created a method to generate a dictionary representation of an instance (method to_dict()).
Now it’s time to re-create an instance with this dictionary representation.
> <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
### 5. Store first object
Now we can recreate a BaseModel from another one by using a dictionary representation:
> <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
### 6. Console 0.0.1
Write a program called console.py that contains the entry point of the command interpreter:
- quit
- help
- empty line
### 7. Console 0.1
Update your command interpreter (console.py) to have these commands:
- create
- show
- destroy
- all
- update
### 8. First User
Write a class User that inherits from BaseModel
### 9. More classes!
Write all those classes that inherit from BaseModel:
- state
- city
- amenity
- place
- review
### 10. Console 1.0
Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review
### 11. All instances by class name
Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all()
### 12. Count instances
Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().
### 13. Show
Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).
### 14. Destroy
Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).
### 15. Update
Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).
### 16. Update from dictionary
Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).
### 17. Unittests for the Console!
Write all unittests for console.py, all features!

# Command interpreter
### How to start it
In the terminal type ./console.py + ente
> $./console.py
> (hbnb) 
### How to use it
##### create an object
> $./console.py
> (hbnb) create BaseModel
##### show an object
> $./console.py
> (hbnb) show <class name> <id instance>
##### destroy an object
> $./console.py
> (hbnb) destroy <class name> <id instance>
##### all an object
> $./console.py
> (hbnb) all
> (hbnb) all <class name>
##### update an object
> $./console.py
> (hbnb) update <class name> <id instance> <attr name> <"attr value"> 

