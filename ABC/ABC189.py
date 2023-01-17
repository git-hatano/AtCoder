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
ans = True
ans = False
print("Yes" if ans else "No")
'''

def A():
    s = input()
    ans = False
    if s[0]==s[1] and s[1]==s[2]:
        ans = True
    print("Won" if ans else "Lost")


"""
%を小数にして使うと小数の誤差でWAになる
"""
def B():
    n, x = map(int, input().split())
    ans = -1
    tmp = 0
    for i in range(n):
        v, p = map(int, input().split())
        # tmp += v*p/100
        tmp += v*p

        # if tmp > x:
        if tmp > x*100:
            ans = i+1
            break
        
    print(ans)


"""
多分探索漏れが起きてる
"""
def C_WA():
    n = int(input())
    a = list(map(int, input().split()))

    l = 0
    r = n-1

    from collections import Counter
    counter = Counter(a)

    ans = 0
    while l<=r:
        x = min(counter.keys())
        num = r-l+1
        ans = max(ans, x*num)
        
        if a[l] < a[r]:
            counter[a[l]] -= 1
            if counter[a[l]]==0:
                del counter[a[l]]
            l += 1
        else:
            counter[a[r]] -= 1
            if counter[a[r]]==0:
                del counter[a[r]]
            r -= 1
            
    print(ans)

"""
全探索はTLE
リストのスライシングがNG
"""
def C_TLE():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for l in range(n):
        for r in reversed(range(l, n)):
            ans = max(ans, min(a[l:r+1])*(r-l+1))
    print(ans)


def C_TLE2():
    n = int(input())
    a = list(map(int, input().split()))

    from collections import Counter
    counter_a = Counter(a)

    ans = 0
    for l in range(n):
        counter_a_tmp = counter_a.copy()
        
        for r in reversed(range(l, n)):
            ans = max(ans, min(counter_a_tmp.keys())*(r-l+1))
            counter_a_tmp[a[r]] -= 1
            if counter_a_tmp[a[r]]==0:
                del counter_a_tmp[a[r]]
            
        counter_a[a[l]] -= 1
        if counter_a[a[l]]==0:
            del counter_a[a[l]]
        
    print(ans)



"""
全探索に辿り着いたのはOK
lを固定して、rの要素と比較すれば良かった
"""
def C_ans():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for l in range(n):
        x = a[l]
        for r in range(l, n):
            x = min(x, a[r])
            ans = max(ans, x*(r-l+1))
    print(ans)


def D_TLE():
    from itertools import product
    n = int(input())
    s = [input() for i in range(n)]
    ans = 0
    for seq in product(range(0, 2), repeat=n+1): # O( 2**(n+1) ) で大きすぎる
        # print(seq)
        y = seq[0]
        for i in range(n):
            if s[i]=="AND":
                y &= seq[i+1]
            else:
                y |= seq[i+1]
        if y==1:
            ans += 1
    print(ans)


"""
https://yamakasa.net/atcoder-abc-189-d-logical-expression/
dp[i][j]: y[i]=jになるときの場合の数
j=0: False
j=1: True
"""
def D_ans():
    n = int(input())
    s = [input() for i in range(n)]

    dp = [[0]*2 for i in range(n+1)]
    dp[0][0] = 1
    dp[0][1] = 1

    for i in range(n):
        if s[i]=="AND":
            # (True/Falseの2通り)*(今までFalseになる場合の数) + (Falseの1通り)*(今までTrueになる場合の数)
            dp[i+1][0] = 2*dp[i][0] + 1*dp[i][1]
            # (Trueの1通り)*(今までTrueになる場合の数)
            dp[i+1][1] = 1*dp[i][1] 
        else: #OR
            # (Falseの1通り)*(今までFalseになる場合の数)
            dp[i+1][0] = 1*dp[i][0]
            # (Trueの1通り)*(今までFalseになる場合の数) + (True/Falseの2通り)*(今までTrueになる場合の数)
            dp[i+1][1] = 1*dp[i][0] + 2*dp[i][1] 
    print(dp[n][1])
