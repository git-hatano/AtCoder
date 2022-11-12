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
    def argmax(x):
        x_max = max(x)
        for i, v in enumerate(x):
            if v == x_max:
                return i
        
    n = int(input())
    h = list(map(int, input().split()))
    ans = argmax(h)+1
    print(ans)


def B():
    nums = list(map(int, input().split()))
    mod = 998244353
    nums = [x%mod for x in nums]

    x = (nums[0]*nums[1]*nums[2])%mod
    y = (nums[3]*nums[4]*nums[5])%mod
    ans = (x-y)%mod
    print(ans)

"""
この問題でPythonならオーバーフローは起きない
"""
def B_ans():
    a, b, c, d, e, f = map(int, input().split())
    mod = 998244353
    ans = (a*b*c - d*e*f)%mod
    print(ans)


"""
正方形判定（２点しか確認していないので本当に正確かは怪しい）
"""
def C():
    def dist(x1, x2):
        return (x1[0]-x2[0])**2 + (x1[1]-x2[1])**2

    #4点が正方形になるかを判定したい
    def check(x):
        d1 = dist(x[0], x[1])
        d2 = dist(x[0], x[2])
        d3 = dist(x[0], x[3])
        ds = sorted([d1, d2, d3])
        
        if not (ds[0]==ds[1] and ds[0]*2==ds[2]):
            return False
        
        d1 = dist(x[2], x[0])
        d2 = dist(x[2], x[1])
        d3 = dist(x[2], x[3])
        ds = sorted([d1, d2, d3])
        
        if not (ds[0]==ds[1] and ds[0]*2==ds[2]):
            return False
        return True

    from itertools import combinations
    s = []
    for _ in range(9):
        s.append(list(input()))
    # "#"の座標を格納
    points = []
    for i in range(9):
        for j in range(9):
            if s[i][j]=="#":
                points.append([i, j])
    #4点を選び、その組み合わせが正方形になるかを判定
    ans = 0
    if len(points) >= 4:
        for p in combinations(points, 4):
            if check(p):
                ans += 1
                # print(p)
    print(ans)


# def D():

