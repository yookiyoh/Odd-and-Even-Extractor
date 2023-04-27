# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 4 - Problem 1
# This program reads a text file that contains a set of integers
# The odd and even integers would be extracted from the main text file inputs and transfer them into separate text files in categorization

# open the numbers.txt file in write mode
with open("numbers.txt", "w") as file:
    # use looping to keep asking the user to input numbers
    while True:
        num_input = input("Enter a number: ")
        # check if the input is a whole number
        try:
            num = int(num_input)
        except ValueError:
            # if not, break out of the loop
            break
        # write the number to the file
        file.write(str(num) + "\n") 

# open the numbers.txt file in read mode
with open("numbers.txt", "r") as file:

# open the even.txt file in write mode and write even numbers to it

# open the odd.txt file in write mode and write odd numbers to it

# print a goodbye message and terminate the program