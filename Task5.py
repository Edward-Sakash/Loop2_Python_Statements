"""Task 5 - find divisible numbers
Your task is to write a Python program using while loop, read (prompt) three numbers (a,b,c) and check how many numbers between a and b are divisible by c.
Input 0 (zero) as a third number (divisor) finishes program and prints out the results.

Your results should look like this:
Type starting integer: 1
Type ending integer: 100
Type divisor: 15


15  is divisible by 15
30  is divisible by 15
45  is divisible by 15
60  is divisible by 15
75  is divisible by 15
90  is divisible by 15


Type starting integer: 5
Type ending integer: 8
Type divisor: 0"""

# Solution 
while True:
    # Prompt the user to enter the starting integer
    start = int(input("Type starting integer: "))
    
    # Prompt the user to enter the ending integer
    end = int(input("Type ending integer: "))
    
    # Prompt the user to enter the divisor
    divisor = int(input("Type divisor: "))
    
    # Check if the divisor is 0
    if divisor == 0:
        break
    
    # Print a blank line before the results
    print()
    
    # Iterate through the numbers between the starting and ending integers
    num = start
    while num <= end:
        # Check if the number is divisible by the divisor
        if num % divisor == 0:
            # Print the number if it is divisible by the divisor
            print(num, "is divisible by", divisor)
        
        # Increment the number
        num += 1
    
    # Print a blank line after the results
    print()
