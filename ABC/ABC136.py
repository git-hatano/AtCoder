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
    a, b, c = map(int, input().split())
    ans = max(0, c-(a-b))
    print(ans)


def B():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if len(str(i))%2 == 1:
            ans += 1
    print(ans)


def C():
    n = int(input())
    h = list(map(int, input().split()))
    m = h[0]
    for i in range(1, n):
        if m < h[i]:
            h[i] -= 1
            m = max(m, h[i])
    
    ans = True
    for i in range(n-1):
        if h[i] > h[i+1]:
            ans = False
    print("Yes" if ans else "No")


"""
2重ループの時点でTLEだが、同じパターンが現れるのを確認することまではできた
10*100後にどのパターンが来ているのかがわからない
"""
def D_WA_TLE():
    s = list(input())
    n = len(s)

    a = [[0]*(n) for i in range(n)]
    for i in range(n):
        a[0][i] = 1

    p = dict()
    row = " ".join([str(x) for x in a[0]])
    p[row] = 0
    for i in range(n-1):
        for j in range(n):
            if s[j]=="R":
                a[i+1][j+1] += a[i][j]
            else:
                a[i+1][j-1] += a[i][j]
        
        row = " ".join([str(x) for x in a[i+1]])
        if row in set(p.keys()):
            before = p[row]
            cur = i+1
            break
        else:
            p[row] = i+1

    idx = 10**100 % (cur-before) + before
    ans = " ".join([str(x) for x in a[idx]])
    print(ans)


"""
ダブリング
dp[p][i]
i番目のマスから2**p回移動した先のマス
"""
def D_ans():
    s = list(input())
    n = len(s)

    dp = [[0]*(n) for i in range(33)]
    #2**0 = 1回目の移動先を格納
    for i in range(n):
        if s[i]=="R":
            dp[0][i] = i+1 #移動先を格納
        else:
            dp[0][i] = i-1
    #2**p回目の移動先を格納
    for p in range(32):
        for i in range(n):
            dp[p+1][i] = dp[p][dp[p][i]]
    #i番目のマスにいる人を2**p回移動させる
    ans = [0]*n
    for i in range(n):
        ans[dp[32][i]] += 1
    print(" ".join([str(x) for x in ans]))
