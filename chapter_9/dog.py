# Making an object from a class is called instantiation, and you work with
# instances of a class.

# Creating and Using a Class

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in respones to a command."""
        print(f"{self.name} rolled over!")

# By convention, capitalized names refer to classes
# in Python. There are no parentheses in the class definition because we’re
# creating this class from scratch.

# The __init__() Method

# A function that’s part of a class is a method. Everything you learned about
# functions applies to methods as well; the only practical difference for now is
# the way we’ll call methods.

# This method has two leading underscores and two trailing
# underscores, a convention that helps prevent Python’s default method
# names from conflicting with your method names. Make sure to use two
# underscores on each side of __init__(). If you use just one on each side, the
# method won’t be called automatically when you use your class, which can
# result in errors that are difficult to identify.

# The line self.name = name takes the value associated with the parameter name
# and assigns it to the variable name, which is then attached to the instance
# being created. The same process happens with self.age = age. Variables that
# are accessible through instances like this are called attributes.


# Making an Instance from a Class

# Think of a class as a set of instructions for how to make an instance. The
# class Dog is a set of instructions that tells Python how to make individual
# instances representing specific dogs.

# Let’s make an instance representing a specific dog:

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Python then returns an instance representing
# this dog. We assign that instance to the variable my_dog. The naming convention
# is helpful here: we can usually assume that a capitalized name like Dog
# refers to a class, and a lowercase name like my_dog refers to a single instance
# created from a class.

# Accessing Attributes
# To access the attributes of an instance, you use dot notation. At v we access
# the value of my_dog’s attribute name by writing:

my_dog.name

# Calling Methods

# After we create an instance from the class Dog, we can use dot notation to
# call any method defined in Dog. Let’s make our dog sit and roll over:

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

# To call a method, give the name of the instance (in this case, my_dog)
# and the method you want to call, separated by a dot. When Python reads
# my_dog.sit(), it looks for the method sit() in the class Dog and runs that
# code. Python interprets the line my_dog.roll_over() in the same way.
# Now Willie does what we tell him to:

# Willie is now sitting.
# Willie rolled over!


# Creating Multiple Instances

# class Dog:
#     --snip--

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# Even if we used the same name and age for the second dog, Python
# would still create a separate instance from the Dog class. You can make
# as many instances from one class as you need, as long as you give each
# instance a unique variable name or it occupies a unique spot in a list or
# dictionary.