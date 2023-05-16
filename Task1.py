"""Task 1 - omitting number
Your task is to write a Python program using while loop to print out numbers from -5 to 5, without 0.
You can't use break and continue statements!

Your results should look similar to this:
-5 -4 -3 -2 -1 1 2 3 4 5"""

# Solution 1
# Set the initial number to -5
number = -5

# Iterate while the number is less than or equal to 5
while number <= 5:
    # Check if the number is not equal to 0
    if number != 0:
        # Print the number
        print(number, end=' ')
    
    # Increment the number by 1
    number += 1

print("_____________________________________________")

