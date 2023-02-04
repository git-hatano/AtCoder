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



def C():
    from collections import defaultdict
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in range(n):
        d[a[i]] += 1
        d[a[i]-1] += 1
        d[a[i]+1] += 1
    ans = 0
    for k in d:
        ans = max(ans, d[k])
    print(ans)


def D():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if i+1==p[i]:
            p[i], p[i+1] = p[i+1], p[i]
            ans += 1
    for i in range(1, n):
        if i+1==p[i]:
            p[i], p[i-1] = p[i-1], p[i]
            ans += 1
    print(ans)
