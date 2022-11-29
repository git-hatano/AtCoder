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
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()

    if u==s:
        a -= 1
    else:
        b -= 1
    print(a, b)


def B():
    s = input()
    ans = "x"*len(s)
    print(ans)


def C():
    n = int(input())
    a = list(map(int, input().split()))
    ans = True
    if n != len(set(a)):
        ans = False
    print("YES" if ans else "NO")


def D():
    from itertools import accumulate
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    #期待値の計算に使う累積和
    a = list(range(1, 1001))
    s = [0] + list(accumulate(a))

    #期待値
    e = []
    for i in range(n):
        e.append(s[p[i]] / p[i])

    #隣り合うk個の最大の期待値を探す. 2重ループにならないように差分を管理
    tmp = sum(e[:k])
    ans = tmp
    for i in range(1, n-k+1):
        tmp -= e[i-1] 
        tmp += e[i+k-1]
        ans = max(ans, tmp)

    print(ans)

