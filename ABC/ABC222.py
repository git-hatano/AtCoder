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
    s = input()
    ans = "0"*(4-len(s)) + s
    print(ans)


def B():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if a[i] < p:
            ans += 1
    print(ans)


def C():
    n, m = map(int, input().split())
    a = []
    for i in range(2*n):
        a.append(input())

    res = []
    for i in range(2*n):
        #[人i, 勝ち数]
        res.append([i, 0])

    for j in range(m):
        for i in range(n):
            #あいこ
            if a[res[2*i][0]][j]==a[res[2*i+1][0]][j]:
                continue
            elif a[res[2*i][0]][j]=="G" and a[res[2*i+1][0]][j]=="C":
                res[2*i][1] += 1
            elif a[res[2*i][0]][j]=="C" and a[res[2*i+1][0]][j]=="P":
                res[2*i][1] += 1
            elif a[res[2*i][0]][j]=="P" and a[res[2*i+1][0]][j]=="G":
                res[2*i][1] += 1
            else:
                res[2*i+1][1] += 1
        #順位の更新
        res = sorted(res, key=lambda x: (x[1], -x[0]), reverse=True)
        
    for i in range(2*n):
        print(res[i][0]+1)


"""
勝ち数にマイナスをつけて、人の名前とセットで管理することで、
rank.sort()
と、ソートを簡単にしている
"""
def C_ans():
    N,M = map(int,input().split())
    S = [input() for i in range(2*N)]
    rank = [[0,i] for i in range(2*N)]
    # rank[i] = [x,y]  -> i位なのは -x勝で人y

    def judge(a,b):
        # 引き分けなら-1,前者勝ちなら0,後者勝ちなら1
        # つまり、買ったほうの番号を返している
        if a==b: return -1
        if a=='G' and b=='P': return 1
        if a=='C' and b=='G': return 1
        if a=='P' and b=='C': return 1
        return 0

    for j in range(M):
        for i in range(N):
            player1 = rank[2*i][1]
            player2 = rank[2*i+1][1]
            result = judge(S[player1][j], S[player2][j])
            if result !=-1: 
                rank[2*i+result][0] -= 1
        rank.sort()
        
    for _,i in rank: 
        print(i+1)


# def D():

