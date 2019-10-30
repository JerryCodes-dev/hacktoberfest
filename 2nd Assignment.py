# NAME : YUSUF JERRY MUSAGA
# MATRIC NUMBER : BHU/19/04/05/0056

# Compute the score of a student to show the grades if the score is inputed

name = input('Enter the name of the student: ')
score = float(input('Enter the score of the student:'))

if score >= 70 and score <=100:
    print(name, 'got an A')
elif score >=60 and score <=69:
    print(name, 'got a B')
elif score >= 50 and score <=59:
    print(name, 'got a C')
elif score >= 45 and score <= 49:
    print(name, 'got an D')
elif score >= 40 and score <= 44:
    print(name, 'got an E')
else:
    print(name, 'got an F')
