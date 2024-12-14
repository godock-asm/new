#Тестовое задание по работе с файлами


file=open('input.py','r')
print(file.read())
file.close()


file=open('input.py','r')
cont=file.readlines()
for el in cont:
    print(el)
    file.close()


with open('input.py', 'r') as file:
    print (file.readline())









