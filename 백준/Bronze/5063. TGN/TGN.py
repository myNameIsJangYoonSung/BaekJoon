t = int(input())

for i in range(t):
    dont, ad, price = map(int, input().split())
    if dont > ad - price:
        print("do not advertise")
    elif dont < ad - price:
        print("advertise")
    else:
        print("does not matter")