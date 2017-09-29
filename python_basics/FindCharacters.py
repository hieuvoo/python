# Find Characters
def findChar(list,char):

    for word in list:
        for letter in word:
            if letter == "o":
                print word
    
findChar(['hello','world','my','name','is','Anna'],'o')