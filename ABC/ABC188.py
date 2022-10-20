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
    m = min(x, y)
    M = max(x, y)

    if m+3 > M:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    tmp = 0
    for i in range(n):
        tmp += a[i]*b[i]
        
    if tmp==0:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def C():
    n = int(input())
    a = list(map(int, input().split()))

    half = (2**n)//2
    a_l = a[:half]
    a_r = a[half:]
    l_max = max(a_l)
    r_max = max(a_r)

    if l_max > r_max:
        ans = a_r.index(r_max) +half +1
    else:
        ans = a_l.index(l_max) +1
    print(ans)



# def D():

