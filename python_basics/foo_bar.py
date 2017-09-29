# def fooBar():
#     for num in range(100,1001):
#         return True
#         for i in range(2, num):
#             if(num%i==0):
#                 prime = False

def perfectsquare(n):
    return not n % n**0.5

perfectsquare(36)

# >>> perfectsquare(37)
# False
# >>> perfectsquare(25)
# True
# >>> perfectsquare(4215378*4215378)
# True