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
    x, y = map(int, input().split("."))
    if 0<=y and y<=2:
        print(str(x)+"-")
    elif 3<=y and y<=6:
        print(x)
    else:
        print(str(x)+"+")


def B():
    n = int(input())
    name = []
    for i in range(n):
        s,t = input().split()
        name.append(s+" "+t)

    if len(name)!=len(set(name)):
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def C():
    n = int(input())

    m = []
    while n:
        if n%2==0:
            m.append("B")
            n = n//2
        else:
            m.append("A")
            n -= 1
    m = m[::-1]
    print("".join(m))


# def D():

