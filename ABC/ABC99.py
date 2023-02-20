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

# def A():



# def B():


"""
選ぶ選ばない+選ぶ場合、いくつにするか

単純な貪欲じゃダメそう
6**1 ~ 6**6
9**1 ~ 9**5
"""
def C_WA():
    n = int(input())
    value = []
    #9
    for i in range(1, 6):
        value.append(9**i)
    #6
    for i in range(1, 7):
        value.append(6**i)
    #1
    value.append(1)
    value.sort(reverse=True)
    ans = 0
    for v in value:
        if n==0:
            break
        if v <= n:
            cnt = n//v
            ans += cnt
            n %= v
    print(ans)


"""
メモ化再帰
"""
def C_ans():
    import sys
    sys.setrecursionlimit(10**9)
    def f(cu):
        if cu==0:
            return 0
        if memo[cu]>0:
            return memo[cu]
        res = float('inf')
        #1yen
        res = min(res, f(cu-1)+1)
        #6yen
        x = 6
        while x<=cu:
            res = min(res, f(cu-x)+1)
            x *= 6
        #9yen
        x = 9
        while x<=cu:
            res = min(res, f(cu-x)+1)
            x *= 9
        
        memo[cu] = res
        return memo[cu]

    n = int(input())
    memo = [0]*(n+10)
    ans = f(n)
    print(ans)


# def D():

