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
    x = int(input())
    ans = (x//100)*100 +100 -x
    print(ans)


def B():
    s = list(input())
    ans = True
    for i, c in enumerate(s):
        if i%2==0 and c.isupper():
            ans = False
        elif i%2==1 and c.islower():
            ans = False
    print("Yes" if ans else "No")


def C():
    n, k = map(int, input().split())
    for i in range(k):
        tmp = []
        for j in str(n):
            tmp.append(j)
        g1 = int("".join(sorted(tmp, reverse=True)))
        g2 = int("".join(sorted(tmp)))
        n = g1 -g2
    print(n)


# def D():

