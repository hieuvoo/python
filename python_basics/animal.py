# Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.
# Animal Class
# Attributes:
#name
#health
#Methods:
#walk: decreases health by one
#run: health decreases by five
#display health: print to the terminal the animal's health.

class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self 
    
    def run(self):
        self.health -= 5
        return self
        # // if self.health <= 0 print " no more health "

    def displayhealth(self):
        print self.name + ": Your health is at " + str(self.health)

# Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.

animal = Animal("Ratata")
animal.walk().walk().walk().run().run().displayhealth()

#Remember that a class is more than just a collection of properties and methods. If you want to create a new class with attributes and methods that are already defined in another class, you can have this new class inherit from that other class (called the parent) instead of copying and pasting code from the original class. Child classes can access all the attributes and methods of a parent class AND have new attributes and methods of its own, for child instances to call.

# # Dog Class
# inherits everything from Animal
# Attributes:
# default health of 150
# Methods:
# pet: increases health by 5
# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().

class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.health = 150
    
    def pet(self):
        self.health += 5 
        return self

dog = Dog("Cerberus")
dog.walk().walk().walk().run().run().pet().displayhealth()

# Dragon Class
# inherits everything from Animal
# Attributes:
#default health of 170
# Methods:
#fly: decreases health by 10
#display health: prints health by calling the parent method and prints "I am a Dragon"

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health = 170
    
    def fly(self):
        self.health -= 10
        return self
    
    def displayhealth(self):
        print "I AM " + self.name + "!!!"
        super(Dragon, self).displayhealth()


dragon = Dragon("SHENRON")
dragon.fly().displayhealth()