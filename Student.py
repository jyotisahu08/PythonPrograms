student = {1:{'Mob':7587149823, 'name':'jyoti', 'age':27, 'dept':'IT', 'Percentage':80},
            2:{'Mob':7349500502, 'name':'Danny', 'age':27,'dept':'CSE','Percentage':87},
         3: {'Mob':78798798878, 'name':'divya', 'age':30, 'dept': 'IT','Percentage':86 }}

# Display all the student details using Registration number
print(student.get(2))

# Adding one more student's details in the dictionary
student[4] = {'Mob':8787678587,'name':'Xyzd', 'age':24,'dept': 'ECE','Percentage':76}
student.setdefault(5,{'Mob':979532332,'name':'nnnnn', 'age':28,'dept': 'CIVIL','Percentage':78})
print(student)

# updating marks of student "Jyoti"
student[1] = {'Percentage':81}
print(student)

# Deleting the particular student details
student.pop(3)
print(student)
