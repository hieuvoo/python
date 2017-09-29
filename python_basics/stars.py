# Create a function called draw_stars() that takes a list of numbers and prints out *.
# For example:

# x = [1,2,3]
# draw_stars(x)should print the following in when invoked:

# *
# **
# ***

def stars(arr):
    for x in arr:
        print "*" * x

nums = [1,2,3]
stars(nums)

def stars2(arr):
    for x in arr:
        if isinstance(x,int):
            print "*" * x
        elif isinstance(x,str):
            length = len(x)
            letter = x[0].lower()
            print letter * length

x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
stars2(x)