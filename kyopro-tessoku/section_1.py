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

def A01():
    n = int(input())
    print(n**2)


def B01():
    a, b = map(int, input().split())
    print(a+b)


def A02():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    a = set(a)
    if x in a:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


# def D():

