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
    a, b, t = map(int, input().split())
    n = int((t+0.5)//a)
    print(b*n)


def B():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = []
    for i in range(n):
        d.append(v[i] - c[i])

    ans = 0
    for i in range(2**n):
        s = 0
        for j in range(n):
            wari = (2 ** j)
            if (i // wari) % 2 == 1:
                s += d[j]
        ans = max(ans, s)
    print(ans)


# def C():



# def D():

