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
print("Yes" if ans else "No")
'''

def A():
    s = input() 
    if s[-1]=="r":
        print("er")
    else:
        print("ist")


def B():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))

    ans = True
    for i1 in range(h-1):
        for i2 in range(i1+1, h):
            for j1 in range(w-1):
                for j2 in range(j1+1, w):
                    if not (a[i1][j1]+a[i2][j2] <= a[i2][j1]+a[i1][j2]):
                        ans = False

    print("Yes" if ans else "No")


def C():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))

    ans = 0
    from itertools import combinations
    for c in combinations(points, 3):
        # print(c)
        s = 1/2 * abs( (c[0][0]-c[2][0])*(c[1][1]-c[2][1]) - (c[1][0]-c[2][0])*(c[0][1]-c[2][1]) )
        if s>0:
            ans += 1

    print(ans)


# def D():

