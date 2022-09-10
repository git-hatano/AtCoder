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
if ans:
    print("Yes")
else:
    print("No")
'''

def A():
    s = input()
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    s = list(s)
    buf = s[a]
    s[a] = s[b]
    s[b] = buf

    ans = "".join(s)
    print(ans)


def B():
    n = int(input())
    a = list(map(int, input().split()))
    x = {}
    for i in range(4*n-1):
        if a[i] not in x:
            x[a[i]] = 1
        else:
            x[a[i]] += 1

    for key in x:
        if x[key] < 4:
            print(key)
            break

def C():
    n, m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())

    from collections import OrderedDict
    x = OrderedDict()
    for i in range(n):
        x[s[i]] = 0

    for j in range(m):
        x[t[j]] += 1

    for key in x:
        if x[key]==1:
            print("Yes")
        else:
            print("No")
    

# def D():

