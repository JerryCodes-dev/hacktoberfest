# NAME : YUSUF JERRY MUSAGA
# MATRIC NUMBER : BHU/19/04/05/0056


# program to find the sum of numbers between 1-100 in step 2

for a in range(1,100,2):
    print(a)

num = 1
while num < 100:
    print(num)
    num += 2


# program to find all even numbers between 1-100

for b in range(2,100,2):
    print (b)

numb = 2
while numb < 100:
    print(numb)
    numb += 2

# program to find the solution to this equation 2x + 3y + 1

x = float(input('Enter a number for x:'))
y = float(input('Enter a number for y:'))
c = 2*(x) + 3*(y) + 1
print(c)

def equation(x,y):
    c = 2*(x) + 3*(y) + 1
    return c
# print in any value for x and y
print(equation(2,3))


# average age of students in class

age = float(input('Enter Age: '))
totalAge = age
sum = 0
while age > 0:
    sum += age
    age -= 1
print('Sum of the ages:', sum)

averageAge = sum / totalAge
print('Average age is: ' , averageAge)
