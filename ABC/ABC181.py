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
    n = int(input())

    if n%2==0:
        print("White")
    else:
        print("Black")


def B():
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        ans += int(1/2 * (b-a+1) * (a+b))
    print(ans)


"""
3点が同一直線上の点か調べる
https://qiita.com/tydesign/items/ab8a5ae52eb9c50ad26a
"""
def C():
    from itertools import combinations
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append([x, y])

    ans = False
    for c in combinations(points, 3):
        dx2 = c[2][0] - c[0][0]
        dy1 = c[1][1] - c[0][1]
        dx1 = c[1][0] - c[0][0]
        dy2 = c[2][1] - c[0][1]
        
        if dx2*dy1 == dx1*dy2:
            ans = True
            break 
        
    print("Yes" if ans else "No")


# def D():

