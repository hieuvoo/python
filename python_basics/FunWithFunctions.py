def odd_even():
for i in range(1,2001):
    if i % 2 == 1:
        print 'Number is '+str(i)+'. This is an odd number.'
    elif i % 2 == 0:
        print 'Number is '+str(i)+'. This is an even number.'         

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

# #HACKER CHALLENGE
def lay_mult(arr):
    print arr
    new_arr = []
    for x in arr:
        val_arr = []
        for i in range(x):
            val_arr.append(1)
        new_arr.append(val_arr)
    return new_arr

x = lay_mult(multiply([2,4,5],3))
print x