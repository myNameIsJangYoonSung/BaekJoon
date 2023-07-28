
a = int(input())
b = input()
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
first = int(str(a*int(b[0]))+"00")
second = int(str(a*int(b[1]))+"0")
third = int(str(a*int(b[2])))

print(first+second+third)