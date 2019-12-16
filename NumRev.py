num = int(input("Enter a number to reverse:"))
rev = 0
rem = 0
while num>0:
    rem = num%10
    rev = rev*10 + rem
    num = num//10
print("Reverse of the given number is",rev)