'''
# 文字列を受け取る場合
s = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
a, b = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# Yes/Noテンプレ
ans = True #ans = False
print("Yes" if ans else "No")

# リストの中身を文字列に
ans = " ".join([str(x) for x in a])
'''

def A():
    n, a, b = map(int, input().split())
    c = list(map(int, input().split()))
    d = a+b
    for i in range(n):
        if c[i]==d:
            print(i+1)
            break


def B():
    import sys
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    b = [list(input()) for _ in range(h)]

    for s in range(h):
        for t in range(w):
            ok = True
            for i in range(h):
                for j in range(w):
                    if a[(i+s)%h][(j+t)%w]!=b[i][j]:
                        ok = False
                        break
            if ok:
                print("Yes")
                sys.exit()
    print("No")




def C():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    n = min(h, w)
    ans = [0]*(n+1)
    
    def test(i, j, d):
        for x in [-d, d]:
            for y in [-d, d]:
                s = i+x
                t = j+y
                if (not (0<=s<h and 0<=t<w)) or c[s][t]!="#":
                    return False
        return True

    for i in range(h):
        for j in range(w):
            if c[i][j]!="#":
                continue
            if test(i, j, 1):
                d = 1
                while test(i, j, d+1):
                    d += 1
                ans[d] += 1
    print(" ".join(str(x) for x in ans[1:]))


import math
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    return prime

def D_TLE():
    from itertools import combinations
    n = int(input())
    root_n = int(math.sqrt(n))
    prime = sieve_of_eratosthenes(root_n)

    facts = []
    for i in range(len(prime)):
        if prime[i]:
            facts.append(i)
    ans = 0
    for c in combinations(facts, 3):
        v = c[0]**2 * c[1] * c[2]**2
        if v <= n:
            ans += 1
    print(ans)


"""
素数の探索範囲の最大値の考察
枝刈りが大切
"""
def D_ans():
    n = int(input())
    ma = 300005 # (10**12)/(2**2 * 3)
    #素数を探索
    prime = sieve_of_eratosthenes(ma)
    p = []
    for i in range(len(prime)):
        if prime[i]:
            p.append(i)
    #答えを探索
    ans = 0
    sz = len(p)
    for i in range(sz):
        #枝刈り1
        vi = p[i]*p[i]*p[i+1]*p[i+2]*p[i+2]
        if vi>n: break
        for j in range(i+1, sz):
            #枝刈り2
            vi = p[i]*p[i]*p[j]*p[j+1]*p[j+1]
            if vi>n: break
            for k in range(j+1, sz):
                v = p[i]*p[i]*p[j]
                #枝刈り3
                if v>n: break
                v *= p[k]
                if v>n: break
                v *= p[k]
                if v>n: break
                ans += 1
    print(ans)
