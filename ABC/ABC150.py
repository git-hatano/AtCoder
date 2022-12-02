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
    k, x = map(int, input().split())
    if 500*k >= x:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    n = int(input())
    s = input()
    key = "ABC"
    ans = 0
    for i in range(n-3+1):
        if s[i:i+3] == key:
            ans += 1
    print(ans)


def C():
    from itertools import permutations
    n = int(input())
    p = "".join([str(x) for x in list(map(int, input().split()))])
    q = "".join([str(x) for x in list(map(int, input().split()))])

    i = 0
    for c in permutations(range(1, n+1), n):
        c = "".join([str(x) for x in c])
        if c==p:
            a = i
        if c==q:
            b = i
        i += 1

    ans = abs(a-b)
    print(ans)


# def D():

