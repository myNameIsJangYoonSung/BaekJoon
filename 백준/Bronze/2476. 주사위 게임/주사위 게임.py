t = int(input())
maxprice = 0
for i in range(t):
    numdict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    first, second, third = map(int, input().split())
    numdict[first] += 1
    numdict[second] += 1
    numdict[third] += 1
    reversedict = {v:k for k,v in numdict.items()}
    
    if max(numdict.values()) == 3:
        if maxprice < 10000 + (first*1000):
            maxprice = 10000 + (first*1000)
    elif max(numdict.values()) == 2:
        if maxprice < 1000 + (reversedict[max(numdict.values())]*100):
            maxprice = 1000 + (reversedict[max(numdict.values())]*100)
    else:
        if maxprice < max(first, second, third)*100:
            maxprice = max(first, second, third)*100
print(maxprice)
