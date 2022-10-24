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
    a = list(map(int, input().split()))
    ans = min(a)
    print(ans)


def B():
    n, m, t = map(int, input().split())
    ans = True
    now_n = n
    now_t = 0
    for i in range(m):
        a, b = map(int, input().split())
        now_n -= (a - now_t)
        if now_n <= 0:
            ans = False
            break
        else:
            now_n = min(n, now_n+(b-a))
            now_t = b

    if ans:
        now_n -= (t - now_t)
        if now_n <= 0:
            ans = False
        
    print("Yes" if ans else "No")


"""
難しく考えすぎ
切るのが可能な場所の選択肢はl-1ヶ所なので、そこから11ヶ所選べば良い
"""
def C_ans():
    import math
    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    l = int(input())
    ans = combinations_count(l-1, 11)
    print(ans)


# def D():

