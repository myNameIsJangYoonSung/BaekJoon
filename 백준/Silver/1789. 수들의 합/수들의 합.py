S = int(input())
num = 1
over = 0
count = 0
while(over < S):
    over += num
    num += 1
    count += 1
if(over == S):
    print(count)
else:
    count -= 1
    print(count)