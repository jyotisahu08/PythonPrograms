f = open('ab.txt','w')
for i in range(0,10):
    f.write("Hello World \n")
f.close()

f=open('ab.txt','r')
for i in range(0,7):
    data = f.readline()
    print(data)
f.close()