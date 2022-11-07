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
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i]==0:
            print(i+1)
            break


def B():
    x, y = map(int, input().split())
    ans = False
    for i in range(x+1):
        turu = i
        kame = x-i
        if 2*turu+4*kame == y:
            ans = True
            break
    print("Yes" if ans else "No")


def C():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))

    ans = x
    if x in p:
        for i in range(1, 10**3):
            buf = []
            a = x-i
            b = x+i
            if a not in p:
                buf.append(a)
            if b not in p:
                buf.append(b)
            if len(buf)>0:
                buf.sort()
                ans = buf[0]
                break
    print(ans)


# def D():

