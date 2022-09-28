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
    x, y = map(int, input().split())
    if x==y:
        ans = x
    else:
        tmp = [0, 1, 2]
        tmp.remove(x)
        tmp.remove(y)
        ans = tmp[0]
    print(ans)


def B():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if a[i]>10:
            ans += (a[i]-10)
    print(ans)


# def C():



# def D():

