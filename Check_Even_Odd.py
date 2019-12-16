num = int(input("Enter a number to check it is even or odd:"))
if num % 2 == 0:
    print("Given number is even")
else:
    print("Given number is odd")

print("given number num = {0} is even")

# List of numbers
list = [45,56,89,41,23,14,34,21,13,1]
evenList = []
oddList = []
for i in range(0,len(list)):
    if(list[i]) % 2 == 0:
        # Adding even numbers to the list
        evenList.append(list[i])
    else:
        # Adding odd numbers to the list
        oddList.append(list[i])
print("The list of even numbers is:", evenList)
print("The list of odd numbers is:", oddList)