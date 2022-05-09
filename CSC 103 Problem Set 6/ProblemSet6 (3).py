#Hope Crisafi
#CSC 103 Problem Set 6
#5/23/21

#NJW 11/20

#Problem 1

#NJW Don't call the function unless I ask you to
#numOne = int(input('Enter a number: '))
#numTwo = int(input('enter another number: '))

def greater_number(firstNum, secondNum):

    if firstNum > secondNum:
        greaterValue = firstNum
        return greaterValue
    else:
        greaterValue = secondNum
        return greaterValue

#print('The greater number is: ',greater_number(numOne, numTwo))



#Problem 2

##score1 = float(input('Enter score 1: '))
##score2 = float(input('Enter score 2: '))
##score3 = float(input('Enter score 3: '))
##score4 = float(input('Enter score 4: '))
##score5 = float(input('Enter score 5: '))


def calc_average(score_1, score_2, score_3, score_4, score_5):
    testAverage = ((score_1 + score_2 + score_3 + score_4 + score_5) / 5)
    return testAverage

def determine_grade(test_average):
    #NJW Should be if/elif/else (-1)
    #NJW You don't need all of these comparisons. Why not?
    if 100 >= test_average >= 90:
        grade = 'A'
        return grade
    if 89 >= test_average >= 80:
        grade = 'B'
        return grade
    if 79 >= test_average >= 70:
        grade = 'C'
        return grade
    if 69 >= test_average >= 60:
        grade = 'D'
        return grade
    if test_average < 60:
        grade = 'F'
        return grade
    #NJW Don't return more or less than you're asked for
    else:
        grade = 'invalid inputs, values entered not within grade range'
        return grade

#NJW SHOULD ask for values in this function (-1)
def question2_driver(calc_average,determine_grade):
    return 'The test average is: '+ str(calc_average) +' and your letter grade is: '+ str(determine_grade)


#testAverage = calc_average(score1, score2, score3, score4, score5)
#grade = determine_grade(testAverage)

#print(question2_driver(testAverage, grade))


#Problem 3

#num = int(input('enter a number: '))


def is_prime(number):
    if number > 1:
        #NJW While loop (-1)
        for remainder in range(2,number):
            if (number % remainder) == 0:
                isPrime = False
                return isPrime
            else:
                isPrime = True
        return isPrime
    else:
        return False

    
#isPrime = is_prime(num)

#NJW Should ask for number (-1)
def is_prime_driver(is_prime):
    #NJW This crashes, because isPrime ISN'T defined (-1)
    if isPrime == True:
        return str(num) + ' is a prime number'
    else:
        return str(num) + ' is not a prime number'

#print(is_prime_driver(isPrime))



# #Problem 4

def prime_numbers():
    primeList =  []

    for num in range(1,101):
        primeNum = is_prime(num)
        if primeNum == True:
            primeList.append(num)

    return 'prime numbers are: ' + primeList

        # if isPrime == True:
        #     print(number)


#print(prime_numbers())


#Problem 5

#numberList = [1, 2, 3, 4.4, 5.5, 6]
#n = 4
#newList = []

#NJW newList must be defined in the function (-1)
def something(numberList, n):

    for num in numberList:
        if n < num:
            newList.append(num)

    return newList
        
#print(something(numberList, n))


#Problem 6

#NJW Why is this not in functions (-2)

filename = 'answers.txt'
myFile = open(filename, 'r')
answersList = (myFile.read())
answersList = answersList.split('\n')

filename2 = 'correct.txt'
myFile2 = open(filename2, 'r')
correctList = (myFile2.read())
correctList = correctList.split('\n')

print('correct answers are:  ', correctList)
print('submitted answers are: ', answersList)

correctAnswersList = []
counter1 = 0
counter2 = 0
index = 0

#NJW This doesn't work (-1)

for line in myFile:
    counter1 += 1

    for line2 in myFile2:

        if correctList[index] == answersList[index]:
            correctAnswersList.append(correctList)
            counter2 += 1
index += 1

print(counter1)
print(correctAnswersList)

if counter2 >= 14:
    print('pass')
else:
    print('fail')


# myFile.close()
# myFile2.close()

#     # counter += 1
#     # for line2 in myFile2:

#     #     if line == line2:
#     #         print('correct')
#     #     else:
#     #         print('incorrect')

# #return correct answers in a single list

# def ggg(index)
