from mypackage.functions import power, average
from mypackage import sayHello, sum, plus

sayHello("Huy Ta")

x = power(3,2)
print("power(3,2) : ", x)

y = sum(3,2)
print("sum(3,2) : ", y)

q = plus(d=3, c=9)
print("plus(9,3) : ", q)

z = average(3,2)
print("average(3,2) : ", z)

fruits = ['mango', 'apple', 'orange']
for fruit in fruits:
	print(fruit)

count = 0
while count < 9:
	count += 1
	print("Count: ", count)

str = 'Hello everybody in the world'
str1 = '0x1101101'

for stri in str:
	print(stri)

print(len(str))
print(str.replace('Hello', 'Goodbye'))
print(str.rfind('world'))
print(str.find('world'))
print(str.split(' '))
print(str.upper())
print(str1.isnumeric())

numbers = [1,2,3,4,5]
numbers2 = [6,7,8,9]

names = ['Huy', 'Binh', 'Hoang', 'Nam', 'Nghia']

print(len(names))

for i in range(0,len(names)):
	print(names[i])

numbers3 = numbers + numbers2
print (numbers3)

del(numbers2[3])
print (numbers2)

names.append('Trung')
print (names)

names.remove('Hoang')
print (names)

mynum = numbers2.pop()
print (mynum)

myloc = str.index('everybody')
print (myloc)

                                                                                                                                                         