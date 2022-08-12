bar = 64
x = int(input())
arr = []

if bar > x:
    while(bar != x):
        bar1 = bar
        if bar1 < x:
            arr.append(bar1)
            x -= bar1
        elif bar1 > x:
            bar = bar1 // 2
        else:
            arr.append(bar1)
print(len(arr)+1)