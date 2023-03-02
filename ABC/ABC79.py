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

# def A():



# def B():



"""
#ワーシャルフロイド法
最短経路問題で使われるアルゴリズムの１つ
グラフ上の全ての頂点間の最短経路を探す
計算量: グラフ上の全ての頂点間の最短経路を探すので O(n**3)

前提知識（ワーシャルフロイド法）以外の方針は良かった
"""
def C_ans():
    h, w = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(10)]
    a = [list(map(int, input().split())) for _ in range(h)]

    #ワーシャルフロイド法: iからjに変換するときの最小値を探索
    for k in range(10): #経由する頂点
        for i in range(10): #始点
            for j in range(10): #終点
                c[i][j] = min(c[i][j], c[i][k]+c[k][j])
    ans = 0
    for i in range(h):
        for j in range(w):
            if a[i][j]>=0:
                ans += c[a[i][j]][1]
    print(ans)


# def D():

