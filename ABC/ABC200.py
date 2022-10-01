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
    n = int(input())
    ans = n//100
    
    if n%100 != 0:
        ans += 1
    print(ans)


def B():
    n, k = map(int, input().split())

    for i in range(k):
        if n%200==0:
            n //= 200
        else:
            n = int(str(n)+"200")
    print(n)    


def C_TLE():
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(a)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            tmp = a[j]-a[i]
            if tmp%200==0:
                ans += 1
    print(ans)


def C_TLE2():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    from itertools import combinations
    for c in combinations(a, 2):
        if abs(c[0]-c[1])%200==0:
            ans += 1

    print(ans)


"""
TLE, 2重ループ対策に使えそう
jを固定
一度見たものを、辞書型で保持しておく感じ
"""
def C():
    n = int(input())
    a = list(map(int, input().split()))
    # 200で割った余りを保持
    b = [x%200 for x in a]

    from collections import defaultdict
    d = defaultdict(int)

    ans = 0
    for i in range(n):
        if b[i] in d:
            ans += d[b[i]]
        d[b[i]] += 1

    print(ans)


# def D():

