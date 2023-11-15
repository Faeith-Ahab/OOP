"""
Object oriented programming (OOP)

Definition
Object Oriented programming is a computer programming concept that models software design around data and objects.
In these data structures, objects are defined and fall under classes with unique attributes, properties, 
while containing unique procedures or methods. 

Advantages/Uses
•	Effortless development and maintenance of projects. 
•	Ensures reusability of code, it enables the programmer to write generic code which can be applied to a range of data. 
•	Software designed using objects is interactive, faster and easier to execute. 
•	OOP provides clear structure for a program.
•	Code is easier to modify, debug and maintain. 
•	It has higher rate of scalability.
•	The OOP is beneficial in collaborative development, there is subdivision of tasks.

Classes
These are blueprints of objects, attributes and methods. 

Objects/Instances
These are instances(occurrences) of a class. 

Exercise
Create a user class with properties i.e., name, age, location.
Create a new instance of the user class (a new object)
Access the user’s name and age.
Create a function for the user class that prints a user’s location.
Print the user’s location using this function.

"""

class Identity:
  def __init__(id, name, age, location): # The id parameter is a reference to the current instance of the class, 
                                         # and is used to access variables that belongs to the class.
                                         # It does not have to be named id , you can call it whatever you like, 
                                         # but it has to be the first parameter of any function in the class.


    id.name = name
    id.age = age
    id.location = location

ResidentOne = Identity("Viv", 100, "Kampala")

print(ResidentOne.name)
print(ResidentOne.age)
print(ResidentOne.location)


ResidentTwo = Identity("Liz", 90, "Entebbe")

print(ResidentTwo.name)
print(ResidentTwo.age)
print(ResidentTwo.location)
