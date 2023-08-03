n = int(input())

while n != -1:
    medicine = []
    for i in range(2,n):
        if n % i == 0:
            medicine.append(i)
    if sum(medicine) + 1 == n:
        print(str(n) + " = 1 + ",end = "")
        for i in range(len(medicine)):
            if i != len(medicine)-1:
                print(str(medicine[i]), end = " + ")
            else:
                print(str(medicine[i]))
    else:
        print(str(n) + " is NOT perfect.")
    n = int(input())