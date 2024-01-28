''' 
T15 - Practical task 1
write a programe that allows a user to register students for an exam venue
and creates/opens and writes to a text file
V1 - Update includes numbers being checks
'''

student_id_list = []        # Empty list to hold student numbers
counter = 0                 # Makes the request for id numbers more user friendly
student_numbers = ""

# Checks user input
while not student_numbers.isdigit() or int(student_numbers)<= 0:
    student_numbers = input("Enter the numbner of students you want to register: ")


for student in range(int(student_numbers)):
  student_id_no = ""
  counter +=1
  # Checks id number of the right length and not repeated
  while not student_id_no.isdigit() or int(student_id_no)<=999 or int(student_id_no)>=10000:
    student_id_no = input(f"Enter the 4 digit id number for student {counter}: ")
    while student_id_no in student_id_list:
      student_id_no = input(f"This number exists, enter a number for a new student {counter}: ")
   
  student_id_list.append(student_id_no)


file_counters = 0
with open("T15/reg_form.txt", "w+") as file:
    file.write("Kingston Venue\n\n")
    file.write("   \t Student No.\t\tStudent signature\n\n")
    for id in (student_id_list):
        file_counters += 1
        file.write(f"{file_counters}.\t\t{id}\t\t    ........................ \n")
        
