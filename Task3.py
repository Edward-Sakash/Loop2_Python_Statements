"""Task 3 - average of numbers
Your task is to write a Python program using while loop, to calculate the average of n integer numbers (input from the user). Input 0 (zero) finishes entering numbers and prints out calculations.

Hint: Average of n numbers is their sum divided by n,
for example average of numbers 5, 7 and 12 is (5 + 7 + 12)/3 = 24/3 = 8.

Your results should look like this:
Input few integers to calculate their average!
Input 0 to exit!!!

Type a integer: 5
Type a integer: 7
Type a integer: 12
Type a integer: 0
Average of the above numbers is:  8.0


<p data-line="64" class="sync-line" style="margin:0;"></p>"""

# Solution 
# Prompt the user to enter integers
print("Input few integers to calculate their average!")
print("Input 0 to exit!!!")

# Initialize variables for sum and count
total = 0
count = 0

# Initialize the first number
number = int(input("Type an integer: "))

# Iterate while the number is not zero
while number != 0:
    # Add the number to the total sum
    total += number
    # Increment the count
    count += 1
    # Prompt the user for the next number
    number = int(input("Type an integer: "))

# Check if count is not zero to avoid division by zero
if count != 0:
    # Calculate the average
    average = total / count
    # Print the average
    print("Average of the above numbers is:", average)
else:
    # Print a message if no numbers were entered
    print("No numbers were entered.")

print("_____________________________________________")


