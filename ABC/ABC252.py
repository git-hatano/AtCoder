
def B():
    N, K = map(int, input().split())
    A = [a for a in list(map(int, input().split()))]
    B = [b-1 for b in list(map(int, input().split()))]

    max_A = max(A)
    res = "No"
    for n in range(N):
        if A[n]==max_A and n in B:
            res = "Yes"

    print(res)


def A():
    n = int(input())
    chr_s = chr(n)
    print(chr_s)


def C_WA():
    n = int(input())
    res = []
    for _ in range(n):
        buf = [0]*10
        S = input()

        for i, s in enumerate(S):
            buf[int(s)] = i
        
        res.append(buf)

    print(res)


def C():
    n=int(input())
    s=[]
    for i in range(n):
        s.append(input())

    cnt = [[0 for j in range(10)] for i in range(10)]
    for i in range(n):
        for j in range(10):
            cnt[int(s[i][j])][j] = cnt[int(s[i][j])][j] +1

    mx = [0 for i in range(10)]
    for i in range(10):
        for j in range(10):
            mx[i] = max(mx[i], 10 * (cnt[i][j]-1) +j)

    print(min(mx))
