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
    n, i = map(int, input().split())
    print(n-i+1)


# def B():


"""
x グラフの最短経路問題?
x 貪欲的に解く?
x 1次元DP?
x 二分探索?
A. 考察問題でした...

1. 最適な動きを考えてみると、負に行って正に行って終えるか、正に行って負に行って終えるのが最適
2. どれだけ負に行くかであるが、負のろうそくをi個経由した場合は正のろうそくをK-i個通る必要がある
3. iを固定するとO(1)で必要な移動量がわかるので、iを全探索すればいい

pr[i] := 原点から正の方向にi個ろうそくを通過するのにかかる時間
mi[i] := ß原点から負の方向にi個ろうそくを通過するのにかかる時間
"""
def C():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    mi = [0]
    pr = [0]
    for i in range(n):
        if x[i] < 0:
            mi.append(-x[i])
        else:
            pr.append(x[i])
    mi.sort()
    pr.sort()

    ans = float("inf")
    n = len(mi)
    m = len(pr)
    #負の方向移動して、正の方向移動
    for i in range(n):
        j = k-i
        if 0<=j<m:
            ans = min(ans, mi[i]*2 + pr[j])
    #正の方向移動して、負の方向移動
    for i in range(m):
        j = k-i
        if 0<=j<n:
            ans = min(ans, pr[i]*2 + mi[j])
    print(ans)


# def D():

