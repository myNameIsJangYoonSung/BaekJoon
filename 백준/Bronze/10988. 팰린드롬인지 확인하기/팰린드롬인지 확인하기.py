palindrome = input()

head = 0
tail = len(palindrome)-1
result = 0
if len(palindrome) == 1:
    result = 1
else:
    while head < tail:
        if palindrome[head] == palindrome[tail]:
            head += 1
            tail -= 1
            result = 1
        else:
            result = 0
            break
print(result)