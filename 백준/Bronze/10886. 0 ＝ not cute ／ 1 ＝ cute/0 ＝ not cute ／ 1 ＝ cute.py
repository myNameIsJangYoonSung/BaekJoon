n = int(input())

newdict = {0:0, 1:0}
for i in range(n):
    cute = int(input())
    newdict[cute] += 1
if newdict[0] > newdict[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")