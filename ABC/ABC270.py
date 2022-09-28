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
    a, b = map(int, input().split())
    c = 0

    xs = [4, 2, 1]
    for x in xs:
        if a>=x or b>=x:
            c += x
            if a>=x:
                a -= x
            if b>=x:
                b -= x

    print(c)


def B():
    x, y, z= map(int, input().split())
    ans = -1
    if x>0:
        if y<0:
            ans = abs(x)
        elif x<y:
            ans = x
        elif z<0:
            ans = abs(z)*2 +x
        elif z>0 and z<y:
            ans = x

    elif x<0:
        if y>0:
            ans = abs(x)
        elif y<x:
            ans = abs(x)
        elif z<0 and y<z:
            ans = abs(x)
        elif z>0:
            ans = 2*z+abs(x)
    print(ans)


"""
深さ優先探索（DFS）
DFSは木構造と相性が良い、らしい
"""
# def C():
n, x, y = map(int, input().split())

to = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    to[a].append(b)
    to[b].append(a)




# dfs(y)

print()
    

# def D():
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# a = sorted(a)

# takahashi = 0
# aoki = 0

# from bisect import bisect_left
# i = 0
# while n>=a[0]:
#     less_n = bisect_left(a, n)
#     if less_n<k and a[less_n]==n:
#         less_n = less_n
#     else:
#         less_n -= 1
    
#     if i%2==0:
#         if less_n>0:
#             takahashi += a[less_n]
#             n -= a[less_n]
#         else:
#             takahashi += a[0]
#             n -= a[0]
#     else:
#         if less_n>0:
#             aoki += a[less_n]
#             n -= a[less_n]
#         else:
#             aoki += a[0]
#             n -= a[0]
#     i += 1

# print(takahashi)

