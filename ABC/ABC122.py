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
    b = input()
    d = {"A":"T", "C":"G", "T":"A", "G":"C"}
    print(d[b])


def B():
    s = input()
    n = len(s)
    w = set(["A", "C", "G", "T"])

    ans = 0
    l = 0
    for i in range(n):
        if s[i] in w:
            l += 1
        else:
            ans = max(ans, l)
            l = 0
    ans = max(ans, l)
    print(ans)


def C():
    n, q = map(int, input().split())
    s = input()
    a = [0]*n
    for i in range(1, n):
        if s[i-1]=="A" and s[i]=="C":
            a[i] += a[i-1]+1
        else:
            a[i] = a[i-1]

    for i in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        ans = a[r] - a[l]
        print(ans)


# def D():

