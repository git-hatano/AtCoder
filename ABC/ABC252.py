
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


n = int(input())
chr_s = chr(n)
print(chr_s)
