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
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    ans = -1
    for i in range(1, n):
        if a[i]-a[i-1]<=d:
            ans = a[i]
            break
    print(ans)


def B():
    import sys
    s = input()
    n = len(s)
    b = []
    for i in range(n):
        if s[i]=="B":
            b.append(i)
    if b[0]%2==b[1]%2:
        print("No")
        sys.exit()

    r_cnt = 0
    ans = False
    for i in range(n):
        if s[i]=="R":
            r_cnt += 1
        elif r_cnt==1 and s[i]=="K":
            ans = True
    print("Yes" if ans else "No")


def C():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w-1):
            if s[i][j]=="T" and s[i][j+1]=="T":
                s[i][j] = "P"
                s[i][j+1] = "C"

    for i in range(h):
        print("".join(s[i]))


def D():
    a = list(map(int, input().split()))
    ans = 0
    while a[0]!=a[1]:
        a.sort()
        c = a[1]//a[0]
        if a[1]>a[0]*c:
            a[1] -= a[0]*c
            ans += c
        else:
            c -= 1
            a[1] -= a[0]*c
            ans += c
    print(ans)


"""
sample3が通らない
多分数え上げができていない
"""
def E_WA():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = []
    for i in range(n):
        ans.append(a[i])

    while True:
        tmp = []
        for i in range(n):
            for v in ans:
                tmp.append(a[i]+v)
        ans += tmp
        ans = list(set(ans))
        if len(ans)>=k:
            break

    ans.sort()
    print(ans[k-1])


# def D_ans():
n, k = map(int, input().split())
a = list(map(int, input().split()))

