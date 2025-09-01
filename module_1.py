# import random library to be able to generate random numbers further
import random

# initialise empty list for generated numbers
rand_numbers = []

# make 100 iterations to generate numbers
for i in range (1,100):

# get random number from range from 1 to 1000
    rand_numbers.append(random.randint(1,1000))

# bubble sort the list
# iterate over entire list
for i in range (0,99):

# for each number iterate over all numbers after it
# and make sure that bigger numbers go to the end of the list
    for j in range (0,99):

# if the number that is closer to the list start is bigger than the one which
# has bigger index - exchange numbers in the list
        if rand_numbers[i] > rand_numbers[j]:
            temp = rand_numbers[i]
            rand_numbers[i] = rand_numbers[j]
            rand_numbers[j] = temp

# initialize variables for count and sum of odd and even numbers
count_odds = 0
count_evens = 0

sum_odds = 0
sum_evens = 0

# iterate over list and find counts and sums for odd and even numbers
for i in range(0,99):

# check if the number is odd, the remainder after dividing by 2 is 0
# for each found number we increase counter by 1 and add it to the respective sum
    if rand_numbers[i] % 2 == 0:
        count_evens += 1
        sum_evens += rand_numbers[i]
    else:
        count_odds += 1
        sum_odds += rand_numbers[i]

# count averages and print them to console
# try/catch block is used to cover edge cases when there are no add or even numbers
try:
    avg_odds = sum_odds / count_odds
    print("The average of odd numbers is: ",avg_odds)
except ZeroDivisionError:
    print ("There are no odd numbers in this range")

try:
    avg_evens = sum_evens / count_evens
    print("The average of even numbers is: ",avg_evens)
except ZeroDivisionError:
    print ("There are no even numbers in this range")