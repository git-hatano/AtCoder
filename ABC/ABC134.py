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
    n = int(input())
    print(3*(n**2))


def B():
    n, d = map(int, input().split())
    ans = n//(2*d+1)
    if n%(2*d+1) != 0:
        ans += 1
    print(ans)


def C():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))

    s_a = sorted(a, reverse=True)
    for i in range(n):
        if a[i]==s_a[0]:
            print(s_a[1])
        else:
            print(s_a[0])


# def D():

