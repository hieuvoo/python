# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
import random

def grade(reps):
    print "Scores and Grades"
    for x in range(0,reps):
        score = random.randint(60,101)
        if score >60 and score <=69:  
            print "Score: "+str(score)+": Your Grade is D"
        if score >70 and score <=79:  
            print "Score: "+str(score)+": Your Grade is C"
        if score >80 and score <=89:  
            print "Score: "+str(score)+": Your Grade is B"
        if score >90 and score <=100:  
            print "Score: "+str(score)+": Your Grade is A"    

grade(10)