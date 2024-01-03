def solution(s):
    answer = []
    print(s)

    for i in range(len(s)):
        if s[i] == "(":
            answer.append(s[i])
        else:
            if len(answer) == 0:
                return False
            else:
                answer.pop()
    if len(answer) != 0:
        return False
    return True