# -*- coding: utf-8 -*-
"""datastruture.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yuz6-oiDE1cUVO4m3SoMZNeC1jNc-kmB
"""

a = [10,20,30,40,50]
for i in a:
  print(i, end="  ")

a = [10,20,30,40,50]
while a:
  print(a.pop(), end="  ")

a = [10,20,30,40,50]
i = 0
while i < len(a):
  print(a[i], end="  ")
  i += 1

a = [10,20,30,40,50]
for i in a:
  if i == 30:
    print("found",i)
    break

a = [10,20,30,40,50]
30 in a

for i in range(4):
  if a[i] == 30:
    print(i)
    break

a = [10,20,30,40,50]
print(a.index(30))

a = [23,4,2,32,43,54,6,576,87,987,34,45,23,43,54,657,76,678,46,43,3,34,54,65,32,54]
len(a)

a[len(a)-1]

info = [1,"ABC",84.9,'a']
print(info)

info[1]

info = [1,"ABC",84.9,'a']
info += "shanda"

print(info)
info[1]="xyz"
print(info)
info[0:3]
info[:0]
info[ :1]
info[ :2]
info[1:]
info[::4]

info[::3]

info[::-1]

a = []
x = 1
while x <= 10:
  a.append(3)
print(a)
x += 1

n = input("enter a number")
a = []
x = 1
while x <= 100:
  a.append(n)
  x += 1
print(a)

a = list(range(1, 20, 2))
print(a)

a = [1,2,3,4,5,6,7,8,9,10]
b = a[::2]
print(b)

a = [1,2,3,4,5,6,7,8,9,10]
b = a[1::2]
print(b)

n = input("enter a number")
a = []
a += n
print(a)

a = input("enter a number")
b = input("enter a number")
c = []
d = []
c.append(a)
d.append(b)
c.extend(d)
print(c)

a = [1,3,4]
b = [5,6,7]
a.extend(b)
print(a)

# prompt: a = [1,3,4]

a = [1, 3, 4]
b = [5, 6, 7]
a.extend(b)
a

a = [1,3,4]
a.insert(1, "2")
print(a)

Tuple = (1,2,3,4,5)
print(Tuple,(type))

value_tuple = (1,2,3,4,5)
value_tuple[0] = 45
print(value_tuple)

value1_tuple = (1,2,3,4,5)
value2_tuple = (6,7,8,9,10)
value3_tuple = value1_tuple + value2_tuple
print(value3_tuple)

value1_tuple = (1,2,3,4,5)
print(value1_tuple[2:])

value1_tuple = (1,2,3,4,5)
print(value1_tuple[:4])

value_tuple = (26,45,'hello',7.5,'z',5,6.9)
print(value_tuple[::-2])

print(value_tuple[1::1])

print(value_tuple[-1::-2])

print(value_tuple[1])

a = [1,7,5,6]
b = max(a)
print(b)

a = [3,10,20,30]
x = 0
for i in a:
  x = x + i
print(x)

a = [3,10,20,30]
b = sum(a)
print(b)

x = "hi how are you"
x.split()

x = int(input("enter a number of element in list"))
a = []
while True:
  y = input("enter a element")
  a.append(y)
  if len(a) == x:
    break
print(a)
y = 0
for i in a:
  y = y + int(i)
print(y)

x = int(input("enter a number of element in list"))
a = []
while True:
  y = input("enter a element")
  a.append(y)
  if len(a) == x:
    break
print(a)
z = set(a)
len(z)

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)



x, y = [int(x) for x in input("Enter two values: ").split()]
print("Number of boys: ", x)
print("Number of girls: ", y)

x, y = [int]

x = int(input())
list_1 = []
for i in range(x):
  list_1.append(int(input()))
print(list_1)

list1 = list(range(1,11))
odd = list1[::2]
print(list1)
print(odd)

list = list(range(1,11))
even = list[1::2]
print(list)
print(even)

n = int(input())
b = []
for i in range(n):
  a = int(input())
  b.append(a)
c = []
d = []
for i in b:
  if i % 2 == 0:
    c.append(i)
  else:
    d.append(i)
print("largest even number:",c[-1])
print("largest odd number:",d[-1])

l1 = []
num1 = int(input("Enter size of list 1 "))
for n in range(num1):
    numbers1 = int(input('Enter number '))
    l1.append(numbers1)
l2 = []
num2 = int(input("Enter size of list 2 "))
for n in range(num2):
    numbers2 = int(input('Enter number '))
    l2.append(numbers2)
union = list(set().union(l1, l2))
print("The union of two lists is:",union)

list1 = [1,2,3,4,3]
c = len(list1)
print(c)
a =sorted(list1)
print(a)
a = 0
z = 0
for i in range(c):
 if list1[a] == list1[a+1]:
   z = z + 1
   a += 1
 else:
  print("0")
print(z)

size_of_list_1=int(input())
list_1=list(map(int,input().split()))
list_1[0]=list_1[0]+list_1[-1]
list_1[-1]=list_1[0]-list_1[-1]
list_1[0]=list_1[0]-list_1[-1]
print(list_1)

Tuple = ("hello")
n = 3
for i in range(int(n)):
  Tuple = (Tuple,)
  print(Tuple)

tuple = ("developer",5,8.9,"r",8)
print(len(tuple))

tuple = (9,5,89,4,8)
print(max(tuple))
print(min(tuple))
print(sum(tuple))

tuple = (4, 1)
print(all(tuple  ))

value_tuple = (26, 45, "hello", 7.5)
print(value_tuple)
value_tuple[2] = "python"
print(value_tuple)

value1_tuple = (26, 45, 'hello')
value2_tuple = (7.5, 5, 6.9)
value3_tuple = value1_tuple + value2_tuple
print(value3_tuple)

value1_tuple = (26, 45, 'hello')
value2_tuple = (7.5, 5, 6.9)
value3_tuple = value1_tuple , value2_tuple
print(value3_tuple)
value1_tuple = value1_tuple + (7,)
print(value1_tuple)

value1_tuple = (26, 45, 'hello')
a = (list(value1_tuple))
print(type(a))
print(a)

value1_tuple = (26, 45, 'hello') * 2
print(value1_tuple)

tuple = ()
list1 = []
x = int(input("no of items"))
for i in range(x):
  n = int(input("enter a number"))
  list1.append(b)
  print(list1)

n = int(input())
list1 = []
for i in range(n):
  a = int(input())
  list1.append(a)
print(tuple(list1))

number = ("one", "two", "three", "four")
i = 0
while i < len(number):
  print(number[i])
  i += 1

number = ("one", "two", "three", "four")
for i in number:
  print(i)

value_tuple = (26, 12, 10, 6, 67, 91, 45, "hello", 7.5, 99, "name")
for i in value_tuple:
  if i == 45:
    print(i)

number = ("one", "two", "three", "four")
(a,*b,d)=number
print(a)
print(*b)
print(d)

a = {2,"python",'a',5,6,}
for i in a:
  print(i)

a = {2,"python",'a',5,6,}
print(7 in a)

a = {2,"python",'a',5,6,}
print('python' in a)

a.add("apple")
print(a)

print(len(a))

a.remove("python")
print(a)

a.discard(5)
print(a)

value_set = {26, 12, 10, 6, 67, 91, 45, "hello", 7.5, 99, "name"}
value_set.append("hello")

value_set = {26, 12, 10, 6, 67, 91, 45, "hello", 7.5, 99, "name"}
value_set.add("apple")
print(value_set)

value_set = {26, 12, 10, 6, 67, 91, 45, "hello", 7.5, 99, "name"}
value_set.add("apple","mango")
print(value_set)

value_set.remove("hello")
print(value_set)

value_set.remove("hello","name")
print(value_set)

value_set.discard("hello")
print(value_set)

value_set.discard(11)
print(value_set)

value_set.clear()
print(value_set)

value_set = {26, 12, 10, 6, 67, 91, 45, "hello", 7.5, 99, "name"}
del value_set
print(value_set)

value_set = set()
n = int(input("enter a number"))
for i in range(n):
  value_set.add(input())
print(value_set)

value_set = {26, 12, 10, 6, 67, 91, 45, "hello", 7.5, 99, "name"}
for i in value_set:
  print(i)

x = str(input("enter a number"))
value_set = {26, 12, 10, 6, 67, 91, 45, "hello", 7.5, 99, "name"}
x in value_set

month1_set = {"January", "February", "March", "April", "May", "June"}
month2_set = {"July", "August", "September", "October", "November", "December"}
month3_set = month1_set.union(month2_set)
print(month3_set)

month1_set = {"January", "February", "March", "April", "May", "June"}
month2_set = {"July", "August", "September", "October", "November", "December"}
month = month1_set | month2_set
print(month)

month1_set = {"jan","feb","mar","apr","jan"}
month2_set = {"may","jun","jul","aug","jan"}
month3_set = month1_set.intersection(month2_set)
print(month3_set)

month1_set = {"jan","feb","mar","apr","jan"}
month2_set = {"may","jun","jul","aug","jan"}
month = month1_set & month2_set
print(month)

diff = (month1_set - month2_set)
print(diff)

x = month1_set.difference(month2_set)
print(x)

month1_set = {"jan","feb","dec","mar"}
month2_set = {"jan","feb", "dec", "mar"}
com = month1_set > month2_set
print(com)
