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
    a, b, c = map(int, input().split())
    print(int(1/2*a*b))


def B():
    def f(n):
        if n%2==0:
            return n//2
        else:
            return 3*n+1

    n = int(input())
    s = set()
    a = []
    for i in range(10**9):
        if i==0:
            s.add(n)
            a.append(n)
        else:
            v = f(a[i-1])
            if v in s:
                break
            s.add(v)
            a.append(v)
    print(i+1)


def C():
    n = int(input())
    h = list(map(int, input().split()))
    h = [0] +h
    d = []
    for i in range(n):
        d.append(h[i+1]-h[i])

    ans = 0
    for i in range(n):
        if d[i]>0:
            ans += d[i]
    print(ans)


# def D():

