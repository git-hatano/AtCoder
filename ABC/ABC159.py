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
    import math
    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    n, m = map(int, input().split())
    ans = 0
    if n>=2:
        ans += combinations_count(n,2)
    if m>=2:
        ans += combinations_count(m,2)
    print(ans)


def B():
    s = input()
    n = len(s)
    ans = True
    if s != s[::-1]:
        ans = False

    s_left = s[:(n-1)//2]
    if s_left != s_left[::-1]:
        ans = False

    s_right = s[(n+2)//2:]
    if s_right != s_right[::-1]:
        ans = False

    print("Yes" if ans else "No")


"""
立方体の時に最大の体積になる、らしい（この問題は知識ゲーで解く？）

体積V
V = x * y * z = x * y * (L-x-y)
連立方程式を
dV/dx = 0
dV/dy = 0
とおいて解くと、
x = y = z = L/3
になった
"""
def C():
    l = int(input())
    ans = (l/3)**3
    print(ans)


"""
初めにボールを抜き取る前の全組み合わせを計算
抜き取るボールに応じて差分を反映し出力
"""
def D():
    from collections import Counter
    import math
    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    n = int(input())
    a = list(map(int, input().split()))

    counter = Counter(a)
    combs = {}   #k: kC2
    combs_dec ={}#k: k-1C2
    comb_total = 0
    for key in counter.keys():
        if counter[key] >= 3:
            comb = combinations_count(counter[key]-1, 2)
            combs_dec[key] = comb
        
        if counter[key] >= 2:
            comb = combinations_count(counter[key], 2)
            combs[key] = comb
            comb_total += comb

    for i in range(n):
        key = a[i]
        if key in combs:
            if counter[key] == 2:
                print(comb_total-1)
            else:
                comb = combs_dec[key]
                comb_total -= combs[key]
                comb_total += comb
                
                print(comb_total)
                
                comb_total -= comb
                comb_total += combs[key]
        else:
            print(comb_total)
