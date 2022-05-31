import datetime

print(datetime.datetime.now())

# //Convert str to int
# s = "4"
# print(type(s))
# print(type(int(s)))
#

# str = 'Python is a programming language'
# print (str.isalnum())
# str = 'This is Interview Question17'
# print (str.isalnum())

a = 1
b = a
print(id(a))
a += 1
print(id(a))

print(id(a))
print(id(b))
b += 1
a = 1
print(id(a))
print(id(b))

