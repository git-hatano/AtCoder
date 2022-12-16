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

def A36():
    n, k = map(int, input().split())
    ans = False
    if k >= 2*n-2 and k%2==0:
        ans = True
    print("Yes" if ans else "No")


def B36():
    n, k = map(int, input().split())
    s = input()
    on = 0
    for c in s:
        if c=="1":
            on += 1

    ans = False
    if on%2 == k%2:
        ans = True
    print("Yes" if ans else "No")


def A37():
    n, m, b = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = sum(a)*m + b*n*m + sum(c)*n
    print(ans)


# def D():
d = {}
def f(n):
    if n in d:
        return d[n]
    elif n < 10:
        d[n] = sum(range(1, n+1))
        return d[n]
    
    sn = str(n)
    return f(int(sn[:len(sn)//2])) + f(int(sn[len(sn)//2:]))

n = int(input())
print(f(n))
