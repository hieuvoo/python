def typeList(list):
    sum = 0
    countInt = 0
    string = ""
    countStr = 0
    
    for value in list:
        x = type (value)
        if x == int or x == float:
            sum += value
            countInt += 1
        elif x == str:
            string = string + " " + value
            countStr += 1
    if countStr > 0 and countInt > 0:
        print "This list has mixed data"
        print "String:", string
        print "Sum:", sum
    elif countStr == len(list):
        print "This list has all strings"
        print "string:", string
    elif countInt == len(list):
        print "This list has all integers"
        print "Sum:", sum
                
# typeList(['magical unicorns', 19, 'hello', 98.98, 'world'])
# typeList([2,3,1,7,4,12])
typeList(['magical','unicorns'])