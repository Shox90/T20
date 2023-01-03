# Create a program to write a text file taking in number of students and their ID numbers
# Output text file to store all user input
text_file = open('reg_form.txt', 'w')

# Create an input variable storing integer from user
students = int(input("How many students are there: "))

# Create a for loop that runs for that amount of students
for student in range(students):
    # For each iteration prompt for input 'ID' assigned to variable id_number
    id_number = input('Enter your ID number: ')
    text_file.write(id_number + "\n")

# Close file to free up resource it is using
text_file.close()
