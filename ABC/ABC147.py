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
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")


def B():
    s = input()
    n = len(s)

    s1 = s[:n//2]
    s2 = s[n//2:]
    s2 = s2[::-1]

    ans = 0
    for i in range(n//2):
        if s1[i] != s2[i]:
            ans += 1
    print(ans)


"""
全bit探索は良かった
問題の意味を理解できなかった
仮説に対して、証言があっているかの確認がなかった
"""
def C_WA():
    n = int(input())
    xy = []
    for i in range(n):
        a = int(input())
        tmp = []
        for j in range(a):
            x, y = map(int, input().split())
            tmp.append([x, y])
        xy.append(tmp)

    ans = 0
    #不誠実な者:0、誠実な者:1の仮定をbit探索で立てる
    for i in range(2**n):
        s = [1]*n
        for j in range(n):
            w = 2**j
            # print(bin(i)[2:].zfill(n), j, w, (i//w)%2)
            if (i//w)%2 == 0:
                s[j] = 0
            else:
                for v in xy[j]:
                    x = v[0]
                    y = v[1]
                    s[x-1] *= y
                
        ans = max(ans, sum(s))
    print(ans)


def C_ans():
    #二進数表記した時の1の個数
    def popcount(n):
        return bin(n).count("1")

    n = int(input())
    #有効グラフで表現
    #g[i][j] 人iが人jのことをどう言っているか
    g = [[-1]*(n) for i in range(n)]
    #証言を格納
    for i in range(n):
        m = int(input())
        for j in range(m):
            x, y = map(int, input().split())
            x -= 1
            g[i][x] = y

    ans = 0
    for i in range(2**n):
        #今の正直者、不誠実者を決める
        d = [0]*n
        for j in range(n):
            w = 2**j
            if (i//w)%2 == 1:
                d[j] = 1
        
        #正直者の証言に矛盾がないかを確認
        ok = True
        for j in range(n):
            if d[j]==1:
                for k in range(n):
                    if g[j][k] == -1:
                        continue
                    if g[j][k] != d[k]:
                        ok = False
        if ok:
            ans = max(ans, popcount(i))
    print(ans)
