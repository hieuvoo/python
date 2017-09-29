# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.
# Then create a new instance called md. It should be able to do the following task:
# MathDojo().add(2).add(2, 5).subtract(3, 2).result
# which should perform 0+2+(2+5)-(3+2) and return 4.
class MathDojo(object):
    def __init__(self):
        self.num = 0
    def add(self, *addnum):
        for i in addnum:
            self.num += i
        return self
    def subtract(self, *subnum):
        for i in subnum:
            self.num -= i
        return self
    def result(self):
        print self.num
        return self.num
md = MathDojo()
md.add(2).add(2, 5).subtract(3, 2).result()

# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. It should now be able to perform the following tasks:
# MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
# should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.

class MathDojoLists(object):
    def __init__(self):
        self.num = 0
    def add(self, *addnum):
        for i in addnum:
            if type(i) == list:
                for j in i:
                    self.num += j
            else:
                self.num += i
        return self
    def subtract(self, *subnum):
        for i in subnum:
            if type(i) == list:
                for j in i:
                    self.num -= j
            else:
                self.num -= i
        return self
    def result(self):
        print self.num
        return self.num
md2 = MathDojoLists()
md2.add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result()

class MathDojoListsTuples(object):
    def __init__(self):
        self.num = 0
    def add(self, *addnum):
        for i in addnum:
            if type(i) == list or type(i) == tuple:
                self.num += sum(i)
            else:
                self.num += i
        return self
    def subtract(self, *subnum):
        for i in subnum:
            if type(i) == list or type(i) == tuple:
                self.num -= sum(i)
            else:
                self.num -= i
        return self
    def result(self):
        print self.num
        return self.num
md3 = MathDojoListsTuples()
md3.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract((2,3,4), [2,3], [1.1, 2.3]).result()