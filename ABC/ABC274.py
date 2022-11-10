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

"""
四捨五入
https://note.nkmk.me/python-round-decimal-quantize/
"""
def A():
    from decimal import Decimal, ROUND_HALF_UP
    a, b = map(int, input().split())
    s = b/a
    s = Decimal(str(s)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
    print(s)


def B():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        s = list(input())
        c.append(s)

    ans = []
    for j in range(w):
        cnt = 0
        for i in range(h):
            if c[i][j]=="#":
                cnt += 1
        ans.append(cnt)

    ans = " ".join([str(x) for x in ans])
    print(ans)


def C():
    n = int(input())
    a = list(map(int, input().split()))

    # k:generation
    d = {1:0}
    for i in range(n):
        d[2*(i+1)] = d[a[i]]+1
        d[2*(i+1)+1] = d[a[i]]+1

    for k in range(2*n+1):
        print(d[k+1])


# def D():

