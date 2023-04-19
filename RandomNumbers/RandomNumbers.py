'''
Random Numbers
Pawelski
4/18/2023
Python II

Instructions:
What is written to the file when you run the program?
What does each line of code do in the program?
What happens when the file does exist and we use the
write ("w") mode? What happens when the file does
exist and we use write ("w") mode?

Modify the code so that it writes 2 random numbers to
the file such that they are on seperate lines. Does
write automatically go to a new line?

Modify the code so that it writes 100 random numbers
to the file such taht they are on seperate lines.
'''

import random

file = open("random_numbers.txt", "w")
number = random.randint(1, 10)
file.write(str(number))
file.close()