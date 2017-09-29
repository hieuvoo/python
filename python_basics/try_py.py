# STRING: capitalize, upper, lower, count, find, index, split, join, replace, format
# LIST: len, max, min, index, append, pop, remove, insert, sort, reverse, (optional) extend, (optional) list

#capitalize, upper
# s = "cotton eye joe"
# print str.capitalize(s)
# print str.upper(s)

# x = 'COTTON EYE JOE'
# print str.lower(x)

# str = 'this is a string example'
# sub = 'i'
# print str.count(sub,0,len(str))

# str = 'this is a string example'
# print str.find('is') 

# str = 'this is a string example'
# sub = 'i'
# print str.index(sub,0,len(str))

# d = 'blue,red,green'
# d.split(',')
# a,b,c = d.split(',')
# print a
# print b
# print c

# y = '-'
# seq = ('a','b','c')
# print y.join(seq)

# y = '-'
# str = 'cotton eye joe'
# str = str.replace('eye','i')
# print str

# a = 'cotton'
# b = 'eye'
# c = 'joe'
# print " where did you come from {} {} {}?".format(a,b,c)

# x = 'COTTON EYE JOE'
# print len(x)

# x = '12345'
# print max(x)
# print min(x)

# list1 = [1,2,3,4,5]
# print list1.index(3)
 
# list1 = [1,2,3,4,5]
# list1.append(666)
# print list1

# list1 = [1,2,3,4,5]
# list1.pop(4)
# print list1

# list1 = [1,2,3,4,5]
# list1.remove(5)
# print list1

# list1 = [1,2,3,4,5,6,7,8,9]
# list1.insert(9,7)
# print list1

# list2 = [3,6,1,9,44,100]
# list2.sort()
# print list2

# list1 = [1,2,3,4,5,6,7,8,9]
# list1.reverse()
# print list1

# aList = [123, 'xyz', 'zara', 'abc', 123];
# bList = [2009, 'manni'];
# aList.extend(bList)
# print "Extended List : ", aList 

x = 'cotton is soft'
print list(x)