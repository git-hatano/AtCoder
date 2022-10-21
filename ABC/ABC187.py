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
    a, b = input().split()
    sa = sum([int(x) for x in a])
    sb = sum([int(x) for x in b])
    ans = max(sa, sb)
    print(ans)


def B():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            a = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
            if abs(a) <= 1:
                ans += 1
    print(ans)


def C():
    n = int(input())
    x0 = set()
    x1 = set()

    for i in range(n):
        s = input()
        if s[0]=="!":
            x1.add(s[1:])
        else:
            x0.add(s)
            
    x_and = x0&x1
    if len(x_and)>0:
        print(list(x_and)[0])
    else:
        print("satisfiable")



# def D():

