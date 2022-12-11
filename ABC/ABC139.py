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
    s = input() 
    t = input() 
    ans = 0
    for i in range(3):
        if s[i]==t[i]:
            ans += 1
    print(ans)


def B():
    import math
    a, b = map(int, input().split())
    ans = 1
    if b==1:
        ans = 0
    elif a<b:
        ans += math.ceil((b-a)/(a-1))
    print(ans)


def C():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    ans = 0
    for i in range(n-1):
        if h[i]>=h[i+1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)


def D():
    n = int(input())
    if n==1:
        ans = 0
    else:
        ans = sum(range(1, n))
    print(ans)
