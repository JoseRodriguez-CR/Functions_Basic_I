#1 Comment: It will print just 5
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 Comment: It will not be printing anything since number_of_days_in_a_week_silicon_or_triangle_sides() has not been defined before
def number_of_military_branches():
    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3 Comment: It will print just 5 and stop the function work, therefore return 10 will not give us that value
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 Comment: It will print just 5 and stop the function work, therefore print(10) will not print in console that value
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 Comment: It will print just 5. Also since function is not returning any value, when print(x) invoke numbers_of_great_lakes thru x it will not return value so probably we get undefined or none
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 Comment: It will print 3 and then 5 because it happens inside the function, but once it will try to print the result of the sum sent to the function, 
# we will not received any value from the function due to lack of return, therefore we will be getting an error 
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7 Comment: It will print a string due to the have the function converting the number into strings and then concatenating them  to return them as string. 
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 Comment: It will print 100 inside the function and then after check the conditional it will return 10 to be printed 
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 Comment: It will print 7 first because of the if, then it will print 14 and finally it will print 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 Comment: It will print 8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 Comment: It will print 500 twice. Then it will print 300 and finally 500. Since no value will be returned "b" won't be changed.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 Comment: It will print 500 twice. Then it will print 300 and finally 500. Since the value was returned but it was not store or 
# updated in "b", this variable won't be changed.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 Comment: It will print 500 twice. Then it will print 300 twice as well. Since "b" was changed inside the function and also the value 
# of b was return and store into "b", this variable became into 300 after invoke the function 
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 Comment: It will print 1, then 3 and finally 2. This is because of the order followed when invoke those functions.
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 Comment: It will print 1, then 3, after that 5 will be printed and finally 10 will be returned and printed. This is 
# because of the order followed when invoke those functions.
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)