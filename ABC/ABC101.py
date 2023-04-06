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



def B():
    s = input()
    n = int(s)
    x = 0
    for c in s:
        x += int(c)
    if n%x==0:
        print("Yes")
    else:
        print("No")


def C():
    import math
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 1
    n -= k
    if n>0:
        ans += math.ceil(n/(k-1))
    print(ans)


# def D():

