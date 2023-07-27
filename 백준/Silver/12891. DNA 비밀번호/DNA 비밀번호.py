s, p = map(int, input().split())
dna = input()
ncount = list(map(int, input().split()))
result = 0
count = {"A":ncount[0], "C":ncount[1], "G":ncount[2], "T":ncount[3]}

start = 0
end = p-1
# print(count["A"],count["C"], count["G"], count["T"])
for i in range(end+1):
    count[dna[i]] -= 1
for i in range(len(dna)-p+1):
    if count["A"] < 1 and count["C"] < 1 and count["G"] < 1 and count["T"] < 1:
        # print(dna[start:end+1],count["A"],count["C"], count["G"], count["T"])
        result += 1
    count[dna[start]] += 1
    start += 1
    if end < s-1:
        end += 1
        count[dna[end]] -= 1
    
print(result)