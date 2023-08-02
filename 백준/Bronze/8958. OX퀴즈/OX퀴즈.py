n = int(input())

for i in range(n):
    jum = 0
    ox = input()
    while "XX" in ox:
        ox = ox.replace("XX", "X")
    if ox[-1] == 'X':
        ox = ox[:-1]
    olist = ox.split('X')
    for j in range(len(olist)):
        jum += len(olist[j])*(len(olist[j])+1)/2
    print(int(jum))
    
