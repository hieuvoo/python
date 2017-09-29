# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 
class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price >= 10000:
            self.tax = "0.15"
        else:
            self.tax = "0.12"
# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

    def display_all(self):
        print "Cars"
        print "Price: $" + str(self.price)
        print "Speed: " + str(self.speed) + " mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + " mpg"
        print "Tax: " + str(self.tax)
        
car1 = Car(2000,35,"Full",15)
car1.display_all()

car2 = Car(2000,5,"Not Full",105)
car2.display_all()

car3 = Car(2000,15,"Half Full",95)
car3.display_all()

car4 = Car(2000,25,"Full",25)
car4.display_all()

car5 = Car(2000,45,"Empty",25)
car5.display_all()

car6 = Car(20000000,35,"Empty",15)
car6.display_all()