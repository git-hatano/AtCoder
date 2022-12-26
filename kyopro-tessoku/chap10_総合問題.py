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

def A71():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)

    ans = 0
    for i in range(n):
        ans += a[i]*b[i]
    print(ans)


"""
白の個数が多い行、列から黒く塗っていく
1WA : こういうケースが通らない
...#
..#.
.#..
.###
"""
def A72_WA():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    #各行の白の個数
    white_row = []
    for i in range(h):
        white = 0
        for j in range(w):
            if c[i][j]==".":
                white += 1
        white_row.append([white, i])
    #各列の白の個数
    white_col = []
    for j in range(w):
        white = 0
        for i in range(h):
            if c[i][j]==".":
                white += 1
        white_col.append([white, j])

    #白の個数が大きい順にソート
    white_row.sort(reverse=True)
    white_col.sort(reverse=True)
    #白の個数が大きい順に、行or列を黒で塗りつぶす: 出力時にカウントしない様にする
    mask_row = set()
    mask_col = set()
    i, j = 0, 0
    for l in range(k):
        if white_row[i][0]-j > white_col[j][0]-i:
            mask_row.add(white_row[i][1])
            i += 1
        else:
            mask_col.add(white_col[j][1])
            j += 1
    #最終的な白の個数をカウント
    white = 0
    for i in range(h):
        if i not in mask_row:
            for j in range(w):
                if j not in mask_col:
                    if c[i][j]==".":
                        white += 1
    ans = h*w-white
    print(ans)


"""
行数の制約が小さいので、行は全bit探索して
その後に余っている回数分だけ白が多い列から塗れば良かった
"""
def A72_ans():
    import itertools
    #残り回の列に対する操作で、最大何個のマスを黒くできるかを返す関数
    def paint_row(h, w, d, remaining_steps):
        #各列に対して（白マスの個数、列の番号）のタプルを記録し、大きい順にソート
        column = [ ([d[i][j] for i in range(h)].count("."), j) for j in range(w) ]
        column.sort(reverse=True)
        
        #列に対して操作を行う
        for j in range(remaining_steps):
            idx = column[j][1]
            for i in range(h):
                d[i][idx] = "#"
        #黒マスの個数を数えて返す
        return sum(map(lambda l: l.count("#"), d)) #行ごとに黒を数えて合計を返す

    h, w, k = map(int, input().split())
    c = [input() for _ in range(h)]

    #行の塗り方を全探索
    ans = 0
    for v in itertools.product([0, 1], repeat=h):
        # print(v)#(0, 1, 1, 0)
        d = [list(c[i]) for i in range(h)]
        remaining_steps = k
        for i in range(h):
            if v[i]==1:
                d[i] = ["#"]*w
                remaining_steps -= 1
        
        if remaining_steps>=0:
            subans = paint_row(h, w, d, remaining_steps)
            ans = max(ans, subans)
    print(ans)


# def D():

