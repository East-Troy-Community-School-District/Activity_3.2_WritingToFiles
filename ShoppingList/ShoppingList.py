'''
Shopping List
Pawelski
4/18/2023
Python II

Instructions:
Currently, the program is missing the code to ask the user
to populate the list called shopping_list. Add the code to
ask the user to enter a series of items or "zzzzz" to quit,
and store these items into the list.

What does the writelines() method do? Does the writelines()
method automatically write each element to seperate lines?
How would you modify the program so that it adds the items
to the end of the file instead of overwriting the file? 
'''

shopping_list = []
# Add your code here!

file = open("shopping.txt", "w")
file.writelines(shopping_list)
file.close()

