n = int(input())

vote = input()
if vote.count(vote[0]) == n:
    print(vote[0])
elif vote.count(list(set(vote))[0])>vote.count(list(set(vote))[1]): 
    print(list(set(vote))[0])
elif vote.count(list(set(vote))[0])<vote.count(list(set(vote))[1]):
    print(list(set(vote))[1])
else:
    print("Tie")
    