# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
    if number %2 == 0:
        even_numbers.append(number)
print(even_numbers)

# 2. Print the difference between the largest and smallest value:
numbers_ascending = sorted(numbers)
# print(numbers_ascending)
largest_number = numbers_ascending[-1]
# print(largest_number)
smallest_number = numbers_ascending[0]
print(largest_number - smallest_number)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
previous_number = 0
for number in numbers:
    if number == 2 and number == previous_number:
        print(number == previous_number and previous_number == 2)
    previous_number = number

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
running_total = 0
should_add = True
for number in numbers:
    if number == 6:
        should_add = False
    if number == 7:
        should_add = True
        running_total = running_total - 7
    if should_add == True:
        running_total = number + running_total
print(running_total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#    So [5, 13, 2] would have sum of 5. 
eventual_sum = 0
counter = -1
unlucky = -100
for number in numbers:
    counter = counter + 1
    if number == 13:
        unlucky = counter
    if counter != unlucky and counter != unlucky + 1:
        eventual_sum = number + eventual_sum
print(eventual_sum)
# counter = -1
# stop_adding = False
# for number in numbers:
#     counter = counter + 1
#     if number == 13:
#         stop_adding = False
#         unlucky = counter
#     if stop_adding == False and counter != unlucky + 1:
#         eventual_sum = number + eventual_sum
# print(eventual_sum)
