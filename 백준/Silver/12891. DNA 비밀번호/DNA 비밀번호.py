# sliding window
s, p = map(int, input().split()) # s = dna 문자열의 길이, p = 패스워드 부분 문자열의 길이
dna = input() # dna 문자열
ncount = list(map(int, input().split())) # 패스워드의 조건
result = 0 # 조건을 충족하는 결과의 갯수를 저장하는 변수
count = {"A":ncount[0], "C":ncount[1], "G":ncount[2], "T":ncount[3]} # 각각의 dna dictionary 생성

start = 0 # two pointer(start)
end = p-1 # two pointer(end)
# print(count["A"],count["C"], count["G"], count["T"])
for i in range(end+1): # 첫 부분합 계산
    count[dna[i]] -= 1
for i in range(len(dna)-p+1): # sliding window
    if count["A"] < 1 and count["C"] < 1 and count["G"] < 1 and count["T"] < 1: # 조건을 만족하면?
        # print(dna[start:end+1],count["A"],count["C"], count["G"], count["T"])
        result += 1 # 결과 + 1
        
    # sliding window 부분
    count[dna[start]] += 1 # start의 dna값에 1을 더해 원상복구
    start += 1 # start 1 증가 (한칸 뒤로)
    if end < s-1: # end가 마지막이 아닐때만
        end += 1 # end 1 증가 (한칸 뒤로)
        count[dna[end]] -= 1 # start에서 하나를 빼주었기 때문에 길이 유지를 위한 end의 dna값에 1을 빼줌
    
print(result)