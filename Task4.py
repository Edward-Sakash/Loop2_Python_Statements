"""Task 4 - find a character
Your task is to write a Python program using while loop, to find indexes of prompted character in the given text.

Note: Program should be case-sensitive, what means that uppercase and lowercase letters are treated as distinct!

Hint: use string's methods and be careful of long texts and new lines!

Note: You can use any text, for example from lyrics. My was:
"She came to me one morning
One lonely Sunday morning
Her long hair flowing in the mid-winter wind
I know not how she found me
For in darkness I was walking
And destruction lay around me from a fight I could not win"

Your results should look like this:
Text:

She came to me one morning
One lonely Sunday morning
Her long hair flowing in the mid-winter wind
I know not how she found me
For in darkness I was walking
And destruction lay around me from a fight I could not win

What should be found?: S

Character S found at index 1
Character S found at index 39


<p data-line="99" class="sync-line" style="margin:0;"></p>"""

# Solution
# Define the input text
text = '''She came to me one morning
One lonely Sunday morning
Her long hair flowing in the mid-winter wind
I know not how she found me
For in darkness I was walking
And destruction lay around me from a fight I could not win'''

# Print the input text
print("Text:\n")
print(text)

# Prompt the user to enter a character to find
character = input("\nWhat should be found?: ")

# Initialize the index variable
index = 0

# Initialize a list to store the indexes of the character
indexes = []

# Iterate while the index is less than the length of the text
while index < len(text):
    # Find the next occurrence of the character starting from the current index
    found_index = text.find(character, index)
    
    # If no further occurrence is found, break the loop
    if found_index == -1:
        break
    
    # Append the found index to the list
    indexes.append(found_index)
    
    # Update the index to search for the next occurrence
    index = found_index + 1

# Print the found indexes
for idx in indexes:
    print(f"Character {character} found at index {idx}")
