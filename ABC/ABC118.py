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
    a, b = map(int, input().split())
    if b%a==0:
        print(a+b)
    else:
        print(b-a)


def B():
    n, m = map(int, input().split())
    l = [0]*m
    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(1, a[0]+1):
            l[a[j]-1] += 1

    ans = 0
    for i in range(m):
        if l[i]==n:
            ans += 1
    print(ans)


def C_WA():
    n = int(input())
    a = list(map(int, input().split()))
    mi = min(a)
    ans = 0
    while True:
        for i in range(1, n):
            a[i] %= mi
        mi = float("inf")
        cnt = 0
        for i in range(n):
            if a[i]>0:
                mi = min(mi, a[i])
                cnt += 1
        if cnt==1:
            break
    print(mi)

# def D():

