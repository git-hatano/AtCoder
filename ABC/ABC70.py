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
最小公倍数
"""
def C():
    import math
    def lcm(x, y):
        return (x * y) // math.gcd(x, y)
    n = int(input())
    t = [int(input()) for _ in range(n)]
    ans = 1
    for i in range(n):
        ans = lcm(ans, t[i])
    print(ans)


# def D():

