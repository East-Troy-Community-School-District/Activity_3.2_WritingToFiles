'''
Product Survey
Pawelski
4/18/2023
Python II

Instructions:
Does the file "survey_results.txt" already exist before the
program runs the first time? Run the program. What does it
do? What happens if you run the program again and enter
more survey results? How many fields does each entry contain?
In what order? Did they have to be in this order? What delimiter
was used to seperate the fields? What is the data type of rating?
'''

file = open("survey_results.txt", "a")

repeat = "y"
while repeat == "y":
    name = input("Enter the name of a product >> ").lower()
    rating = input("Enter the rating for the product (1 - 5) >> ")
    file.write(name + "," + rating + "\n")
    repeat = input("Enter another rating? (y/n) >> ").lower()
    print()

file.close()
