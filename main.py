
file=open('new.txt', 'r')
cont=file.read()
file2=open('main.py', 'w')
file2.write(cont)
file2.close()
file.close()
a=5
b=2
c=3
print((a+b)*c)
