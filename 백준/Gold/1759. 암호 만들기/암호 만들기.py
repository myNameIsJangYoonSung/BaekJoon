def dfs(n, cnt, password):
    if n == C:
        if len(password)==L and cnt >= 1 and L-cnt >= 2:
            ans.append(password)
        return
    
    dfs(n+1, cnt+table[ord(pw_lst[n])], password+pw_lst[n])
    dfs(n+1, cnt, password)


L, C = map(int, input().split())
pw_lst = sorted(input().split())
table = [0]*128 # ascii 코드는 127번 까지 있음

for st in "aeiou": 
    table[ord(st)] = 1

ans = []
dfs(0, 0, "") # n층, 모음의 갯수, pw 문자열

for pw in ans:
    print(pw)