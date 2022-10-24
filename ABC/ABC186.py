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
    n, w = map(int, input().split())
    ans = n//w
    print(ans)


def B():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a += list(map(int, input().split()))
        
    min_a = min(a)
    ans = 0
    for i in range(h*w):
        if a[i] != min_a:
            ans += (a[i] - min_a)
    print(ans)


def C():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        d = list(str(i))
        o = list(oct(i)[2:])
        if "7" not in d and "7" not in o:
            ans += 1
    print(ans)


"""
TLE対策: sort + 累積和
sortで絶対値をはずせるので、シグマを一つ消せる
→ O(N**2) から O(N*logN)
"""
def D_ans():
    from itertools import accumulate
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(a)
    s = [0] + list(accumulate(a))

    ans = 0
    for i in range(n):
        ans += (s[n] - s[i]) - (n-i)*a[i]

    print(ans)


"""
累積和なしver
なしというよりは途中で累積和を求めていってる
"""
def D_ans2():
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(a)
    s = 0
    ans = 0

    for j in range(n):
        ans += a[j]*j - s
        s += a[j]

    print(ans)

