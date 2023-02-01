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
    n = int(input())
    s = input()

    if s[n-1]=="o":
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    p = list(map(int, input().split()))
    s = ""
    for i in range(len(p)):
        s += chr(p[i]-1+97)
    print(s)


"""
https://qiita.com/u2dayo/items/35df8435c7e79fd07eeb#c%E5%95%8F%E9%A1%8Cshapes
これで緑ってまじですか
"""
def C_ans():
    def count_sharp(s):
        ret = 0
        for s_row in s:
            ret += s_row.count("#")
        return ret

    def find_first_sharp(s):
        n = len(s[0])
        for row in range(n):
            for col in range(n):
                if s[row][col]=="#":
                    return row, col

    def is_same(s, t, dr, dc):
        n = len(s[0])
        for row in range(n):
            for col in range(n):
                row_s = row + dr
                col_s = col + dc
                if 0 <= row_s < n and 0 <= col_s < n:
                    if s[row_s][col_s] != t[row][col]:
                        return False
                else:
                    if t[row][col]=="#":
                        #グリッドから # がはみ出ているため
                        return False
        return True

    def rot(s):
        return list(zip(*s[::-1]))

    def judge(s, t):
        # #の数が同じか
        if count_sharp(s) != count_sharp(t):
            return False
        #回転用のfor
        for _ in range(4):
            #sの1番左上の#の位置
            sr, sc = find_first_sharp(s)
            #tの1番左上の#の位置
            tr, tc = find_first_sharp(t)
            #平行移動する量を計算
            dr = sr - tr
            dc = sc - tc
            
            if is_same(s, t, dr, dc):
                return True
            #tを90度回転 
            t = rot(t)
        return False

    n = int(input())
    s = []
    for i in range(n):
        s.append(list(input()))
    t = []
    for i in range(n):
        t.append(list(input()))
    print("Yes" if judge(s, t) else "No")


"""
4点を選んで長方形になるかを確認
nC4は流石にTLE
"""
def D_TLE():
    from itertools import combinations
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for c in combinations(a, 4):
        #x or y軸に並行な辺が1つでもあるか
        flag = False
        for i in range(1, 4):
            if c[0][0]==c[i][0] or c[0][1]==c[i][1]:
                flag = True
                break
        if not flag:
            continue
        
        #対角線が重心で交わるか
        mx = (c[0][0]+c[1][0]+c[2][0]+c[3][0])#/4
        my = (c[0][1]+c[1][1]+c[2][1]+c[3][1])#/4
        
        d_pow2 = (4*c[0][0]-mx)**2 + (4*c[0][1]-my)**2
        res = True
        for i in range(1, 4):
            d_pow2_tmp = (4*c[i][0]-mx)**2 + (4*c[i][1]-my)**2
            if d_pow2!=d_pow2_tmp:
                res = False
                break
        if res:
            ans += 1
    print(ans)


"""
2点（左上、右下）を決めて、
残りの2点（右上、左下）が存在するかをカウント
"""
def D_ans():
    n = int(input())
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    s = set()
    for i in range(n):
        s.add((x[i], y[i])) #set()にタプルなら入る
    ans = 0
    for i in range(n):
        for j in range(n):
            if x[i]<x[j] and y[i]<y[j]: #左上、右下の関係にあるか
                if (x[i], y[j]) in s and (x[j], y[i]) in s: #右上、左下の点があるか
                    ans += 1
    print(ans)
