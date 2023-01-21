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
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    tmp1 = a[p-1:q]
    cnt1= 0
    tmp2 = a[r-1:s]
    cnt2 = 0
    for i in range(n):
        if p-1<=i<=q-1:
            b.append(tmp2[cnt2])
            cnt2 += 1
        elif r-1<=i<=s-1:
            b.append(tmp1[cnt1])
            cnt1 += 1
        else:
            b.append(a[i])
    ans = " ".join([str(x) for x in b])
    print(ans)


def B():
    n = int(input())
    s = input()
    ans = []
    i = 0
    while i<n:
        if i<n-1 and s[i]=="n" and s[i+1]=="a":
            ans.append("nya")
            i+=2
        else:
            ans.append(s[i])
            i+=1
    print("".join(ans))


"""
問題文に騙された
計算量をちゃんと考えて丁寧に解けばWA減らせた
"""
def C():
    n, a, b = map(int, input().split())
    s = list(input())

    ans = float("inf")
    for i in range(n):
        tmp = a*i
        if i>0:
            s.append(s[0])
            del s[0]
        for j in range(n//2):
            if s[j]!=s[n-1-j]:
                tmp += b
        ans = min(ans, tmp)
    print(ans)



"""
単純な貪欲じゃ合わない
"""
def D():
    n, x = map(int, input().split())
    v = []
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(b):
            v.append(a)
    v.sort(reverse=True)

    cur = 0
    ans = False
    for i in range(len(v)):
        if cur+v[i] <= x:
            cur += v[i]
    if cur==x:
        ans = True
    print("Yes" if ans else "No")


"""
貪欲法で解けないコインの問題はナップサック問題
"""
def D():
    n, x = map(int, input().split())
    v = []
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(b):
            v.append(a)
    """
    dp[i][j] : i枚目までの合計金額j円
    """
    r = len(v)
    c = x+10**3
    dp = [[0]*(c+10) for i in range(r+1)]
    dp[0][0] = 1
    for i in range(r):
        for j in range(c):
            if dp[i][j]>0:
                dp[i+1][j] = 1 #そのコインを選ばない
                if j+v[i]<c:
                    dp[i+1][j+v[i]] = 1 #そのコインを選ぶ
    ans = False
    if dp[r][x]==1:
        ans = True
    print("Yes" if ans else "No")
