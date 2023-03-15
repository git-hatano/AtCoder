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
    v, t, s, d= map(int, input().split())
    if v*t <= d <= v*s:
        ans = False
    else:
        ans = True
    print("Yes" if ans else "No")


def B():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = []
    for i in range(n):
        if a[i] != x:
            ans.append(str(a[i]))
    print(" ".join(ans))


"""
問題文自体が良くわからん
"""
def C_ans():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        s = input()
        grid.append([1 if c=="#" else 0 for c in s])# "#"を1, "."を0に変換

    ans = 0
    for row in range(h-1):
        for col in range(w-1):
            #2x2マスの正方領域を全探索
            cnt = 0
            cnt += grid[row][col]    #左上
            cnt += grid[row][col+1]  #右上
            cnt += grid[row+1][col]  #左下
            cnt += grid[row+1][col+1]#右下
            
            if cnt==1:
                ans += 1
            elif cnt==3:
                ans += 1
    print(ans)


# def D():

