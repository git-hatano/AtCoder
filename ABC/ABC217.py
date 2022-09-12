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
    s,t = input().split()
    x = sorted([s, t])

    if s==x[0]:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    s = []
    for _ in range(3):
        s.append(input())

    x = ["ABC", "ARC", "AGC", "AHC"]
    diff = set(s) ^ set(x)
    print(list(diff)[0])

def C():
    n = int(input())
    p = [x-1 for x in list(map(int, input().split()))]

    q = [0]*n
    for i in p:
        q[p[i]] = i
    print(" ".join([str(x+1) for x in q]))


# def D():

