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
全探索: 間に合わん
2分探索?
DP: dp[i][j] 3*(10**5)ならいける?
"""
def C_TLE():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i] < b[j] < c[k]:
                    ans += 1
    print(ans)


"""
2分探索までは合ってた、実装できなかった
"""
def C_ans():
    from bisect import bisect_left, bisect_right
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for i in range(n):
        #aの中でb[i]より小さい個数
        aa = bisect_left(a, b[i])
        #cの中でb[i]より大きい個数
        cc = n - bisect_right(c, b[i])
        ans += aa*cc
    print(ans)


# def D():

