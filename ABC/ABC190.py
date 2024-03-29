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

from tkinter import N


def A():
    a, b, c = map(int, input().split())
    if a>b:
        ans = "Takahashi"
    elif b>a:
        ans = "Aoki"
    else:
        if c==0:
            ans = "Aoki"
        else:
            ans = "Takahashi"
    print(ans)


def B():
    n, s, d = map(int, input().split())
    ans = False
    for i in range(n):
        x, y = map(int, input().split())
        if x<s and d<y:
            ans = True
    print("Yes" if ans else "No")


"""
ボールの置き方を全bit探索を使って全探索し、
一番条件に合っている置き方を探す

itertools.product(直積) と *(シーケンスのアンパック)
を使うともっとスッキリ書ける
https://atcoder.jp/contests/abc190/editorial/626
"""
def C():
    #input
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        a, b = map(int, input().split())
        ab.append([a-1, b-1])
        
    k = int(input())
    cd = []
    for i in range(k):
        c, d = map(int, input().split())
        cd.append([c-1, d-1])
    #process
    ans = 0
    for bit in range(1 << k):
        bit = bin(bit)[2:].zfill(k)
        n_list = [0]*n
        for i in range(k):
            n_list[cd[i][int(bit[i])]] += 1
        
        ans_tmp = 0
        for i in range(m):
            if n_list[ab[i][0]]>=1 and n_list[ab[i][1]]>=1:
                ans_tmp += 1
        ans = max(ans, ans_tmp)
        
    print(ans)


"""
2*n と O(sqrt(2*n)) に観察して気付けたのはよかった
"""
def D_WA():
    import math
    n = int(input())
    ans = 0
    for i in range(1, int(math.sqrt(n*2))+1):
        #nが奇数
        if n%2==1 and (n*2)%i==0:
            ans += 2
        #nが偶数
        if n%2==0 and i%2==1 and (n*2)%i==0:
            ans += 2
    print(ans)


"""
等差数列の和 N
N = 1/2*n*(2*a +n -1)
↓
2*N/n = 2*a-1 : 奇数になる
n: 項数, a: 初項
"""
def D_ans():
    import math
    n = int(input())
    ans = 0
    for i in range(1, int(math.sqrt(n*2))+1):
        if (2*n)%i==0:
            #約数の小さい方
            d = i
            if (2*n//d - d)%2==1:
                ans += 1
            #約数の大きい方
            d = (2*n)//i
            if (2*n//d - d)%2==1:
                ans += 1
    print(ans)

