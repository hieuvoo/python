#find and replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
words = words.replace("day", "month")
print words

#min and max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]
x2 = [x[0],x[len(x)-1]]
print x2

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
list1 = x[:len(x)/2]
list2 = x[len(x)/2:]
list2.insert(0,list1)
print list2