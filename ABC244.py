
def D():
    S = input().split()
    T = input().split()

    cnt = 0
    for i in range(3):
        if S[i] != T[i]:
            j = T.index(S[i])
            S[i], S[j] = S[j], S[i]

            cnt+=1

    if cnt%2==0:
        print("Yes")
    else:
        print("No")



