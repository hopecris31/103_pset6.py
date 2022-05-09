#Hope Crisafi
#5/9/2021
#Practice Set 5

#NJW 16/18

#NJW DO NOT COMMENT OUT CODE


#Part 1

# number = int(input('enter a number: '))
# product = number * 10

# while product < 10000:
#     product = product * 10
#     print(product)



#Part 2

#NJW DO you need this before the loop?

# num1 = int(input('enter your first number: '))
# num2 = int(input('enter your second number: '))
# numSum = num1 + num2

# print('the sum of the numbers is: ',numSum)

# operationRepeat = input('do you want to repeat this operation? (enter yes/no): ')

# while operationRepeat == 'yes':
#     num1 = int(input('enter your first number: '))
#     num2 = int(input('enter your second number: '))
#     numSum = num1 + num2
#     print('the sum of the numbers is: ',numSum)

#     operationRepeat = input('do you want to repeat this operation? (enter yes/no): ')

#NJW DO YOU NEED to check this every time INSIDE the loop? (-1)

#     if operationRepeat == 'no':
#         print('Operation Complete')



#Part 3

# number = 100

#NJW FOR LOOP (-1)

# while number < 1000:
#     if number % 17 == 0:
#         print(number)
#     number += 1


#range of all 3 digit numbers
#if numbers are % == 0 by 17
#print the number


# #Part 4

# speed = int(input('enter vehicle speed: '))
# hoursTraveled = int(input('enter hours traveled: '))
# distance = 0

#NJW Can you use the range function to start at hour 1?

# for hour in range(hoursTraveled):
#     hour += 1
#     distance += speed
#     print(hour, ':', distance)
    


#Part 5

# integer = int(input('enter a positive integer: '))
# numSum = 0

# while integer > 0:
#     numSum += integer
#     integer = int(input('enter a positive integer: '))
    
# print(numSum)




#Part 6

population = int(input('enter number of organisms: '))
dailyIncrease = float(input('enter percentage: '))
increasePercent = dailyIncrease / 100
days = int(input('number of days to multiply: '))
populationIncrease = days * increasePercent #1.5



for day in range(population):
    day += 1
    populationIncrease += increasePercent #5 * .3
    #population *
    print(day, ':', "{:.1%}".format(populationIncrease))

