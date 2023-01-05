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
    k = int(input())
    a, b = map(int, input().split())
    ans = False
    if (a - a%k + k) <= b or a%k==0 or b%k==0:
        ans = True
    print("OK" if ans else "NG")


"""
小数の誤差でWAが1つでる
"""
def B_WA():
    x = int(input())
    s = 100
    ans = 0
    while x > s:
        s += int(s/100)
        ans += 1
    print(ans)


def B_ans():
    x = int(input())
    s = 100
    ans = 0
    while x > s:
        s *= 101
        s //= 100
        ans += 1
    print(ans)


"""
dの大きい順にA[i]を決定
一度決定した後の条件の反映する方法が分からない
"""
def C_WA():
    n, m, q = map(int, input().split())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))

    query = sorted(query, key=lambda x: (-x[3], x[0]))
    A = [1]*n
    ans = 0
    for i in range(q):
        a, b, c, d = query[i]
        a -= 1
        b -= 1
        if A[b]==1:#?
            A[b] = A[a]+c
            ans += d
    print(ans)


"""
n, m が小さいので、数列Aを全探索
単調増加しているようなAの候補を列挙するのがまず大変
https://qiita.com/u2dayo/items/386142030a70d2db4e58
"""
def C_ans():
    #『重複組み合わせ』を列挙する関数: 求めたい配列Aの候補を簡単に生成できる
    from itertools import combinations_with_replacement as comb_rplc
    n, m, q = map(int, input().split())
    req = [list(map(int, input().split())) for _ in range(q)]

    ans = 0
    for seq in comb_rplc(range(1, m+1), n):
        #seq: nが3なら, (1,1,1), (1,1,2), ..., (m,m,m) のような数列
        score = 0
        for a, b, c, d in req:
            #インデックスを0始まりに
            if seq[b-1] - seq[a-1] == c:
                score += d
        ans = max(ans, score)
    print(ans)


def D_TLE():
    a, b, n = map(int, input().split())
    ans = 0
    for x in range(n+1):
        tmp = int(a*x/b) - a * int(x/b)
        # print(x, ans, tmp)
        ans = max(ans, tmp)
    print(ans)


def D():
    a, b, n = map(int, input().split())
    if n >= b-1:
        x = b-1
    else:
        x = n
    ans = int(a*x/b) - a * int(x/b)
    print(ans)
