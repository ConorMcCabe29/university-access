## 15 Different print statements 
### Print is a very versatile command in python and there are many way to use it, shown below are 15 examples of the print statement being used.

# Print a String
To print a string in python you must place "" inside the brackets of the print statement.
```Python
print("Hello world\n")
```
# Print variable
Printing a variable is when you are printing something that you have predifined, shown below i defined ```toprint``` as ```"Wexford is the greatest county\n"``` as such when i print ```toprint``` it prints what i defined it as.
```Python
toprint = "Wexford is the greatest county\n"
print(toprint)
```
# Print an input
Below it takes what you type into the console the ```input``` and print that according to what else is written.
```Python
print("Hi, " + input() + " You're the best\n")
```
# Printing a dict
A dict is a table of information used in python and this is how it's printed.
```Python
print({'county': 'Wexford', 'location': 'South-east'})
```
# Separator argument
The separator argument is used in a print statement to set what will be used between the multiple strings.
```Python
print('Conor', 'McCabe\n', sep=' Richard ')
```
# Numbers
## Int
An Int is a full round number.
```Python
print(int(15))
```
## Float
A float is a number with a decimal.
```Python
print(float(15.5))
```
# Line breaks
A line break is caused by putting ```\n``` where you want the break to happen.
```Python
print("\nHello Enda\nWexford is the greatest county\n")
```
# Questions
This is an example of an ```if``` statement plus usage of ```input``` in the ```if``` statement.
```Python
print('What is the best county?')
county = input("Enter county name: ")
print(county)

if county == "wexford":
    print("You're correct well done.")
else:
    print("You're wrong it's Obviously Wexford.")
```
# Loops
## For loop
This is a ```for``` loop where it prints everything in the list.
```Python
family = ["Phil", "Tracey", "Roisin", "Conor", "Aoife"]
for x in family:
  print(x)
```
## While loop
This is a ```while``` loop where it will keep repeating until ```w``` is not less than 22.
```Python
w = 10
while w < 22:
    print(w)
    w += 2
```
## Range
This will print everything in the set ```range```.
```Python
q = range(10)
for n in q:
    print(n)
```
# Print to a file
This is a method of how to print an input directly into a file.
```Python
import sys
print("What do you want to print to the file? ")
original_stdout = sys.stdout # change where im outputting to

with open('/home/conormccabe/Desktop/test_file.txt', 'w') as f:
    sys.stdout = f # outputting to file
    print(input())
    sys.stdout = original_stdout # output changed back to original
```
# Current time
This will print the current time.
```Python
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")  #string for the current time
print("Current Time =", current_time)
```



# References
**[Real Python - Calling print](https://realpython.com/python-print/#calling-print)**
**[stackabuse - Write to a file](https://stackabuse.com/writing-to-a-file-with-pythons-print-function/)**
**[w3schools - Loops](www.w3schools.com)**
**[Real Python - More loops](https://realpython.com/python-while-loop/)**
**[StackoverFlow - Input printing](https://stackoverflow.com/questions/22917903/text-game-if-statement-based-of-input-text-python/34610789)**
