# Intinput Function

This repository contains a Python function named `intinput` which prompts the user to input an integer value. 
If the user inputs a non-integer value, the function will display an error message and prompt the user again until a valid integer is entered.

## Parameters
- prompt (str): The message displayed to the user when asking for input.
- err (str, optional): The error message displayed when the user inputs a non-integer value. Defaults to "Invalid input, please enter an integer.".

## Installation
```
!pip install intinput
```
## Example Usage
### - Without Error Command
```
from IntInput import intinput

# Using the function with the default error message
result = intinput("Enter an integer: ")

# Use the result in your code
print("You entered the number:", result)
```
### - With Error Command
```
from IntInput import intinput

# Store the returned value in a variable
result = intinput("Please enter a number: ", "This is not a number, try again.")

# Use the result in your code
print("You entered the number:", result)
```
