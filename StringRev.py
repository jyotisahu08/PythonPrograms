from builtins import print

str = 'High Time'

# Printing length of given string
a = len(str)
print('Length of the given string is :',a)

# Printing reverse of the given string
str1 = ""
for i in str:
	str1 = i + str1
print("Reverse of given string is :",str1)

# Checking a given string is palindrome or not
str2 = 'abba'
str3 = ''
for i in str2:
	str3 = i + str3
assert str2==str3,"given string is not a palindrome"
print("given string is a palindrome")

# Displaying the string multiple times
for i in range(0,3):
	 print(str)
