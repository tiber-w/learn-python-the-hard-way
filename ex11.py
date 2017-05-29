import datetime

print("What's your name?", end = ' ')
name = input()
print("How old are you?", end = ' ')
age = int(input())
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

year = datetime.datetime.now().year
print("So, %s was born in %d, %s tall and %s heavy." % (
    name, year - age, height, weight))
print("So, %r was born in %r, %r tall and %r heavy." % (
    name, year - age, height, weight))
