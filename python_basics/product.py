class product(object):
    def __init__(self,price,item,weight,brand,cost,status="For Sale"):
        self.price = price
        self.item = item
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    #Methods:
    # Sell: changes status to "sold"
    # Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    # Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.
    def sell(self):
        self.status = "Sold"
        return self

    def addtax(self,tax):
        self.price *= tax

    def returns(self,reason):
        if reason == "defective":
            self.status = "Defective"
            self.price = 0
        elif reason == "in box":
            self.status = "For sale"
        elif reason == "open box":
            self.status = "Used"
            self.price *= .8
    # Display Info: show all product details.
    def displayInfo(self):
        print "Price: $ " + str(self.price)
        print "Item name: " + str(self.item)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Cost: " + str(self.cost)
    
print "YUGIOH CARDS"
product1 = product(7.99,"Yugioh Cards","5oz","Bandai",5)
product1.returns("in box")
product1.displayInfo()

print "DYSON VACUUM"
product2 = product(499.99,"Vacuum","15 lbs","Dyson",5)
product2.returns("open box")
product2.displayInfo()

print "MICROWAVE"
product1 = product(19.99,"Microwave","1oz","GE",5)
product1.returns("defective")
product1.displayInfo()