t = int(input())

for i in range(t):
    n = int(input())
    schooldict = {}
    for j in range(n):
        name, drink = input().split()
        drink = int(drink)
        schooldict[name] = drink
    reversedict = {v:k for k,v in schooldict.items()}
    print(reversedict[max(schooldict.values())])