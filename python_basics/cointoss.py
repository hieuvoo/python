import random

def cointoss(reps):

    attempt = 1
    counth = 0
    countt = 0
    result = ""
    result_string = ""

    for x in range(1,reps):
        toss = random.randint(0,1)
        if toss == 1:
            counth += 1
            result = "head"
            print "Attempt #", attempt, ": Coin result ", result, " Got ", counth, "head(s) so far and", countt, "tail(s) so far"
        else:
            countt += 1
            result = "tail"
            print "Attempt #", attempt, ": Coin result ", result, " Got ", countt, "head(s) so far and", counth, "tail(s) so far"
        attempt += 1
    
cointoss(5001)


#my code is not working
# if tails == 0:
#         result1 = "tails"
#         countt += 1
#         print '   far'
#     elif heads != 0:
#         result2 = "heads"
#         counth += 1 
#         print 'Attempt #'+str(i)+': Coin Thrown: '+result2+' Got '+str(counth)+' tail(s) so far and '+str(countt)+' tails(s) so far'