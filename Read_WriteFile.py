# Writing data into a file
f = open("abc.txt","w")
f.write("My name is jyoti sahu")
f.close()

# Reading data from a file
f = open("abc.txt","r")
print(f.read())
f.close()

# Copying the contents of file1 to file2
f = open("abc.txt","r")
f.c