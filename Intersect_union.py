list1 = [8,9,7,1,35,8,37,2,4,1,4,5]
a = list1.__len__()
print(a)
list2 = [7,6,8,2,5,67,98,100,6,8]
b = list2.__len__()
print(b)

# Union Of two list
c = list1+list2
s = set(c)
print("The union of given two lists is : ",s)

# Intersection of two list
list3 = (set(list1)&set(list2))
print("The intersection of given two lists is : ",list3)