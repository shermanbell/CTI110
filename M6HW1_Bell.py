#Sherman_Bell
#CTI_110
#M6HW1_Test Average and Grade
#8_Nov_2017

# Write a program that asks the user to enter five test grads.
# The program should then display a letter grade for each score, and finally the average test score
#Write the following function for the program

# main()- this function will control the main flow of the program. It will call the next two function to do most of the work
# It should also hold the input() commands to allow the user to type in grades

# calc_average() - this function should accept five test score(int or float) as arguments, and return the average of the scores.
# In order to calculate an average,(you should take the total of all grades, and then divide it by the number of grades.)

# determine_grade() - This function should accept a test score(int or float) as an argument and return a letter grade for the score.
# Use the ten- point grading scale you used in a previous assigment
# The letter grade, a string , should be  A, B, C, D OR F.

def enterTheScore():
    score1 = float( input( "Please enter first score:  ") )
    score2 = float( input( "Please enter second score:  ") )
    score3= float( input( "Please enter next score:  ") )
    score4= float( input( "Please enter next score:  ") )
    score5= float( input( "Please enter last score:  ") )

    return score1, score2, score3, score4, score5

def cal_average( score1, score2, score3, score4, score5) :
        average = ( score1 + score2 +  score3 +  score4 + score5 ) / 5
        print( " Avg Score\t Letter Grade")
        print( str(average) + "\t" +  determine_grade(average))       
        return average
    
def determine_grade( userScore ):
        if( userScore < 60) : return "F"
        elif( userScore < 70) : return "D"
        elif( userScore <80 ) : return "C"
        elif(userScore < 90) : return "B"
        elif(userScore < 101): return "A"
        
def printTableOfResults( score1, score2, score3, score4, score5) :
        print( "Score\tLetter Grade")
        print( str( score1 ) + "\t" + determine_grade( score1 ))
        print( str( score2 ) + "\t" + determine_grade( score2 ))
        print( str( score3 ) + "\t" + determine_grade(score3 ))
        print( str( score4 ) + "\t" + determine_grade( score4 ))
        print( str( score5 ) + "\t" + determine_grade( score5 ) )

def main() :               
    score1, score2, score3, score4, score5 = enterTheScore()
    print()
    printTableOfResults( score1, score2, score3, score4, score5)
    print()
    cal_average( score1, score2, score3, score4, score5)
   

main()
    
        
            
