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
    if a>=13:
        print(b)
    elif 6<=a<=12:
        print(b//2)
    else:
        print(0)


def B():
    r, d, x = map(int, input().split())
    for i in range(10):
        x = r*x -d
        print(x)


def C():
    n, m = map(int, input().split())
    l = [None]*m
    r = [None]*m
    for i in range(m):
        l[i], r[i] = map(int, input().split())

    ans = max(0, min(r) - max(l) +1)
    print(ans)


# def D():

