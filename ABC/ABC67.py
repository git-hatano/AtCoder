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
累積和
"""
def C():
    from itertools import accumulate
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] + list(accumulate(a))
    ans = float("inf")
    for i in range(1, n):
        x = s[i]
        y = s[n] - s[i]
        ans = min(ans, abs(x-y))
    print(ans)


# def D():

