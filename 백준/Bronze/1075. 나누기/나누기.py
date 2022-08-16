n = eval(input())
f = eval(input())
remainder = n//100 % f
if remainder == 0:
    print("00")
else:
    remainder = remainder * 100
    while(remainder % f != 0):
        remainder += 1
    remainder = remainder % 100
    if remainder < 10:
        print('0', remainder, sep="")
    else:
        print(remainder)