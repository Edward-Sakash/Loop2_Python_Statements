"""Task 2 - Upper and lower letters
Your task is to write a Python program using while loop, that iterates over given string and converts the lower letters to capital letters and vice versa.
Print it out after changes.

Hint: use string's methods and be careful of long texts and new lines!

Note: You can use any text, for example from lyrics. My was:
"Overhead the albatross
Hangs motionless upon the air
And deep beneath the rolling waves
In labyrinths of coral caves" 😃

Your results should look like this:
oVERHEAD THE ALBATROSS hANGS MOTIONLESS UPON THE AIR aND DEEP BENEATH THE ROLLING WAVES iN LABYRINTHS OF CORAL CAVES


<p data-line="43" class="sync-line" style="margin:0;"></p>"""

# Solution 1
# Define the input string
text = "Overhead the albatross\nHangs motionless upon the air\nAnd deep beneath the rolling waves\nIn labyrinths of coral caves"

# Initialize an empty string to store the modified text
modified_text = ""

# Initialize the index for the while loop
index = 0

# Iterate while the index is less than the length of the string
while index < len(text):
    # Get the current character
    char = text[index]
    
    # Check if the character is a lowercase letter
    if char.islower():
        # Convert the lowercase letter to uppercase
        modified_text += char.upper()
    # Check if the character is an uppercase letter
    elif char.isupper():
        # Convert the uppercase letter to lowercase
        modified_text += char.lower()
    else:
        # Append the character as it is
        modified_text += char
    
    # Increment the index
    index += 1

# Print the modified text
print(modified_text)
