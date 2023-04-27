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
    # read all the lines and convert them to integers
    numbers = [int(line.strip()) for line in file.readlines()]

# create empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# sort the numbers in ascending order
numbers.sort()

# iterate over the numbers and extract even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        print("Even number found: {num}!")
    else:
        odd_numbers.append(num)
        print("Odd number found: {num}!")

# open the even.txt file in write mode and write even numbers to it
with open("even.txt", "w") as file:
    file.write("\n".join(str(num) for num in even_numbers))

# open the odd.txt file in write mode and write odd numbers to it
with open("odd.txt", "w") as file:
    file.write("\n".join(str(num) for num in odd_numbers))

# print a goodbye message and terminate the program
print("\nThank you for using this program!")
print("Program terminating in...")
for i in range(3, 0, -1):
    print("{i}")
exit()

# testing