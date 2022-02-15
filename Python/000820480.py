# I, Yash Chaudhary, student number 000820480, certify that all code
# Submitted is my own work; that I have not copied it from any other source.
# I also certify that I have not allowed my work to be copied by others.


import random

# Module 

# for rolling Single dice, parameter as number of sides

def rollDie( faces ):   
    return random.randint(1,faces)


# Validting Interger in terms of type & Range

def validateInt(_min,_max, prompt ):
    int_valid = False               # Initializing loop
    while not int_valid :           # loop that run until user type in valid Integer
        num = input(prompt)         # Taking Input
        
        if num.isdecimal():         # validating Integer
            num = int(num)
            if (num >= _min) and (num <= _max) :    # validating range
                int_valid = True
            else :
                print('It is not valid positive integer, Try Again !')
        else :
            print('It is not valid positive integer, Try Again !')
            
    return num


# Validating String, listOfChoices is list that has to match user input 

def validateStr(prompt, listOfChoices):
    str_valid = False                   # to Intialize loop
    while not str_valid:                # loop that run until user type in valid string
        string = input(prompt)          # prompting for input

        if string.lower() in listOfChoices :    
                str_valid = True

        if not str_valid :
            print('Sorry, this is not a valid input, try again!')

    return string.lower()


# To find average of value inside of list

def average( inList ):          # inList is list which average needs to be find
    listLength = len( inList )

    Sum = 0                     # Intitializing Sum
    for i in inList :           # loop to which access every value in list add it to sum
        Sum += i

    avg = round(Sum / listLength)
     
    return Sum, avg


# To calculate percentage as required in Game
def calculatePercentage( faces, dice, Sum):
    percentage =  Sum / (faces * dice)
    
    return percentage


# To Whehter check the if the number is prime number

def isPrime( number ):
    prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]

    if number in prime :
        ans = True
    else :
        ans = False
        
    return ans


# Pattern 1 
def pattern1( rolledDice ):       # rolledDice is list of dice 
    ans = True                  
    for i in rolledDice :         # loop to access every value inside of List
        if rolledDice[0] != i :   # checking if any value is not equal to the value at first place 
            ans = False           # Using if a = b and b = c then a = c, If every digit is equal to first digit then all are same
                
    return ans

# Pattern 2
def pattern2( sum_ ):           # sum_ is the sum of rolled dice
    if isPrime( sum_ ):         # checking if sum is prime, isPrime defined above
        ans = True
    else :
        ans = False
        
    return ans

# Pattern 3
def pattern3( average, rolledDice):  # average of the rolled dice, rolledDice is list of dice that are rolled
    count = 0                        # counting the number of dice which are above the average
    
    for i in rolledDice :
        if i >= average :
            count += 1

    if ( count >= (len(rolledDice)/2) ):
        ans = True
    else :
        ans = False
            
    return ans

# Pattern 4
def pattern4( rolledDice ):         # list of rolled dice
    ans = True                      # ans holds whether pattern 4 matched
    n = len(rolledDice)
    for i in range(n-1):            # TO loop until Last Second indices of list
        for z in range(i+1,n):      # To loop from indices one greater than above till last indices of list 
            if rolledDice[i] == rolledDice[z]:      # chech if the value are same
                ans = False

    return ans 

# function to check Bonus Factor, many parameter are used as they are required to check the CONDITION to validate the pattern

def bonusFactor( faces, dice, rolled, Sum, average):

    ## alloting bonus for pattern 1 ## 
    if faces >= 4 :                                                     # Checking Condition for Pattern 1
        if pattern1( rolled ):                                          # as pattern1() matched
            print('Pattern 1 matched because, all dice are equal')
            factor1 = 10                                                # factor1 holds the points
        else :                                                          # if pattern not matched
            print('Pattern 1 not matched because, some dices are different')  
            factor1 = 0
    else :                                                              # if Condition for pattern 1 not matched
        print('pattern 1 does not apply because, sides of dice are not greater than or equal to 4')
        factor1 = 0
        
    ## alloting bonus for pattern 2 ##
    if (faces*dice) >= 20 :                                                  # Checking Condition for Pattern 2
        if pattern2( Sum ):                                                  # as pattern2() matched 
            print('Pattern 2 matched, sum of the dice is', Sum,'which is a prime number')
            factor2 = 15
        else :                                                               # if pattern2 not matched
            print('Pattern 2 not matched, sum of the dice is', Sum,'which is not a prime number')
            factor2 = 0
    else :                                                                   # if Condition for pattern 2 not matched
        print('Pattern 2 not applicabel since the maximum score is not greater than or equal to 20')
        factor2 = 0
        
    ## alloting bonus for pattern 3 ##
    if dice >= 5 :                                                           # Checking Condition for Pattern 3
        if pattern3( average, rolled ) :                                     # if pattern3() matched 
            print('Pattern 3 matched as Half of the rolled dice', rolled,' are greater than the average', average)
            factor3 = 5
        else :                                                              # if pattern3 not matched
            print('Pattern 3 not matched as Half of the rolled dice', rolled,' are not greater than the average', average)
            factor3 = 0
    else :                                                                  # if Condition for pattern 3 not matched
        print('Pattern 3 not applicable as the number of dice rolled', rolled,' are smaller than 5 ')
        factor3 = 0
        
    ## alloting bonus for pattern 4 ##
    condition1 = dice > 4                           # Checking Condition 1 for Pattern 4
    condition2 = faces > dice                       # Checking Condition 1 for Pattern 4
    if condition1 and condition2 :              
        if pattern4( rolled ) :                                              # if pattern4() matched
            print('Pattern 4 matched all the rolled dice', rolled,' are of different value')
            factor4 = 8
        else :                                                               # if pattern4 not matched
            print('Pattern 4 not matched all the rolled dice', rolled,' are not of different value')
            factor4 = 0
    else :                                                                      # if Condition for pattern 4 not matched
        factor4 = 0
        if condition1 :                                                         # if Condition 1 is matched but condition 2 not matched
            print('Pattern 4 not applicable because the sides of the dice are not greater than the number of dice rolled')
        elif condition2 :                                                       # if Condition 2 is matched but condition 1 not matched
            print('Pattern 4 not applicable because the number of dice rolled are not greater than 4')
        else :                                                                  # if Condition 1 and Condition 2 not matched
            print('Pattern 4 not applicable sincbecause the sides of the dice are not greater than the number of dice rolled and the number of dice rolled are not greater than 4')

    ## alloting bonus for pattern 5 ##
    if (factor1 + factor2 + factor3 + factor4) == 0 :
        print("pattern 5 matched since you didn't matched any pattern")
        factor5 = 1
    else :                                                  # if pattern5 not matched
        print("pattern 5 not matched since, you have matched one of the above pattern")
        factor5 = 0

    bonusFactor = factor1 + factor2 + factor3 + factor4 + factor5
    print('Your Bonus Factor is ',bonusFactor)
    
    return bonusFactor

# Calculating Score with 4 parameter that are required to calculate it
def score( BonusFactor, dice, faces, Sum ):         
    myStudentNumber = int('000820480')

    Score = int(BonusFactor * calculatePercentage( faces, dice, Sum)) + (myStudentNumber % 500) # calculatePercentage() is defined ahead
     # int() used above is to truncate to the decimal point 
    return Score


                                    ######      ######      ######      ######      ######      ######
                                                              #### MAIN ####
#
scoreList = []              # List to store final score of each turn
playAgain = True            # To Intialize the loop for game
turn = 1                    # counting turn
listOfChoices = ['yes','no']
listOfChoices0 = ['y','n']

print("COMP 10001 –W2020 Final Project by Yash Chaudhary, Student Number: 000820480 \
\n Welcome To the Dice Game, Enjoy!")

print('')

prompt = ('Enter the Number of Sides of dice you want to play with, between [2,20]')
faces = validateInt( 2, 20, prompt)                                                 # faces is number of sides of dice

print('')

prompt = ('Enter the Number of Dice you want play with, between [3,6]')
dice = validateInt( 3, 6, prompt)


## GAME LOOP Started
while playAgain :                                   # Game loop that will run until user wants to play

    print('')
    rolled = []                                     # rolled is list that contain rolled dice
    for i in range(dice):                           # Loop which runs 'dice' times to roll single dice
        rolled.append(rollDie( faces )) 

    print('You rolled', rolled)

    Sum = average( rolled )[0]
    Average = average( rolled )[1]

    print('Sum of your dies is', Sum, "and average ", Average)
    print('')
    
    BonusFactor = bonusFactor( faces, dice, rolled, Sum, Average)      # This will print the bonus Factor along with, How patterns matched or not
    print('')
    
    Score = score( BonusFactor, dice, faces, Sum )
    print('The score of your dice are', Score,' Points')

    print('')
    
    prompt = ('Do you want to reroll any Dice[yes/no]: ')               
    rollagain = validateStr(prompt, listOfChoices)                     # Asking User whether he wants to reroll die 

    # Reroll Process Start
    if rollagain == 'yes' :                             
        n = 0                                                           # to Initalize the loop
        reRolled = []                                                   # creting new list of rerolled dice that will store boolean whether to reroll 
        while n < dice :
            prompt = ('Do you want to Reroll Dice '+ str(n+1)+' ['+ str(rolled[n])+'] ("y"/"n"): ')  # asking user to reroll with dice number and value 
            roll = validateStr(prompt, listOfChoices0)
            if roll == 'y' :
                reRolled.append(True)
            else :
                reRolled.append(False)

            n += 1

        prompt = ('Are you sure you want to reRoll [yes/no]')           # Asking again to Confirm if he user wants to reroll
        rollagain = validateStr(prompt, listOfChoices)

        if rollagain == 'yes':  
            n = 0                                                   # To Intitalize the loop 
            while n < dice:                                         # Loop that will MODIFY the "rolled" according to user input of 'rerolled'
                if reRolled[n] :
                    rolled[n] = rollDie( faces )                    # modifying the index value that user asked for
                n += 1

            print('')    
            print('You have Rolled',rolled)             

            # Following the same step of showing Bonus point and score
            Sum = average( rolled )[0]
            Average = average( rolled )[1]
            print('')
            
            print('Sum of your dies is', Sum," and average ",Average)
            print('')
            
            BonusFactor = bonusFactor( faces, dice, rolled, Sum, Average)
            print('')
            
            Score = score( BonusFactor, dice, faces, Sum )
            print('The score of your dice are', Score,' Points')
    # Reroll Process END

    print('')
    if turn == 1 :                                              # If above was the first turn then, start game again.
        print("This was your First turn, let's play again")
        palyAgain = True
        turn += 1
        print('')
        print('------- Turn 2------')
    else :                                                   # If above was not First turn then showing them avgScore and asking to play again..
        avgScore = average( scoreList )[1]                   # Calculating average score of the previous turns to compare with this turn
        
        if Score > avgScore :
            print('Your Score', Score,'on turn', turn,'which was above average')
        elif Score == avgScore :
            print('Your Score', Score,'on turn', turn,'which was average')
        else :
            print('Your Score', Score,'on turn', turn,'which was below average')

        print('')     
        prompt = ('Do you want to play the game again ["yes"/"no"]: ')          # Asking If User wants to play again
        playAgain = validateStr(prompt, listOfChoices)

        if playAgain == 'yes':
            playAgain = True
            turn += 1
            print('')
            print('------- Turn', turn,'------')                            # This is to show the Turn which they are going to play
        else :
            playAgain = False
            print('------ Result -------')


    scoreList.append( Score )                           # Adding this turn score to scoreList that records score of all turns
    
## GAME LOOP ENDED  ##
    
print('')
avgScore = average( scoreList )[1]
print('You played', turn,'times today with average score of', avgScore)

print('                                                          --------------  END  ---------------')
