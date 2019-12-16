# Swapping using temporary variable
a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
temp = 0
print("Value of a and b before swapping:", 'a = ',a,'b = ',b)
temp = a
a = b
b = temp
print("Value of a and b after swapping:", 'a = ',a,'b = ',b)

# Swapping without using temporary variable
a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
print("Value of a and b before swapping:", 'a = ',a,'b = ',b)
a = a + b
b = a - b
a = a - b
print("Value of a and b after swapping:", 'a = ',a,'b = ',b)