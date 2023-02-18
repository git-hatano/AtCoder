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
    n = int(input())
    if n==25:
        print("Christmas")
    elif n==24:
        print("Christmas Eve")
    elif n==23:
        print("Christmas Eve Eve")
    elif n==22:
        print("Christmas Eve Eve Eve")


def B():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    ans = 0
    for i in range(n):
        if i==n-1:
            ans += p[i]//2
        else:
            ans += p[i]
    print(ans)


def C():
    n, k = map(int, input().split())
    h = []
    for i in range(n):
        h.append(int(input()))
    h.sort(reverse=True)

    ans = float("inf")
    for i in range(n-k+1):
        ans = min(ans, h[i]-h[i+k-1])
    print(ans)


def D_TLE():
    n, x = map(int, input().split())
    cur = "P" #level0
    for i in range(n):
        tmp = []
        tmp.append("B")
        tmp.append(cur)
        tmp.append("P")
        tmp.append(cur)
        tmp.append("B")
        cur = "".join(tmp)

    ans = 0
    for i in range(x):
        if cur[i]=="P":
            ans += 1
    print(ans)


"""
https://blog.hamayanhamayan.com/entry/2018/12/09/101457
再帰的な構造を含む問題は、大体再帰関数を使って解く、らしい
"""
def D_ans():
    import sys
    sys.setrecursionlimit(10**9)
    n, x = map(int, input().split())
    x -= 1
    patty = [0]*51 #レベルlevelバーガーに含まれるパティの数
    tot = [0]*51   #レベルlevelバーガーの層数

    #各レベルでの数をあらかじめ計算
    tot[0] = 1
    patty[0] = 1
    for i in range(1, n+1):
        tot[i] = tot[i-1] *2 +3
        patty[i] = patty[i-1] *2 +1

    def f(level, x): #再帰関数よく分からん
        #level=0なら、パティ1枚なので1を返す。
        if level==0: 
            return 1
        
        #それ以外なら、下からx番目のxが5パーツに別れてるうちのどこに含まれるかを見る
        if x<1: #x=0 : バン1枚
            return 0
        x -= 1
        
        if x < tot[level-1]: #1≦x≦tot[level-1] : レベルL-1バーガー
            return f(level-1, x)
        x -= tot[level-1]
        
        if x<1: #x=tot[level-1]+1 : パティ1枚
            return patty[level-1]+1
        x -= 1
        
        if x < tot[level-1]: #tot[level-1]+2≦x≦2*tot[level-1]+1 : レベルL-1バーガー
            return patty[level-1]+1 + f(level-1, x)
        x -= tot[level-1]
        
        return patty[level-1]*2 +1 #x=tot[level-1]+2 : バン1枚

    print(f(n, x))


# def D():

