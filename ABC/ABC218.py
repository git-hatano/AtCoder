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



# def D():

