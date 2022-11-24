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
    n = int(input())
    ans = int(n/2+0.5)
    print(ans)


def B():
    def check_bingo(x):
        #縦
        for j in range(3):
            tmp = 0
            for i in range(3):
                tmp += x[i][j]
            if tmp==3:
                return True
        #横
        for i in range(3):
            if sum(x[i])==3:
                return True
        #斜め
        if x[0][0] + x[1][1] + x[2][2] == 3:
            return True
        if x[0][2] + x[1][1] + x[2][0] == 3:
            return True
        return False

    a = [list(map(int, input().split())) for _ in range(3)]
    #a:(i,j)
    pos = {}
    for i in range(3):
        for j in range(3):
            pos[a[i][j]] = [i, j]
    #ビンゴシート
    check = [[0]*3 for i in range(3)]

    n = int(input())
    for i in range(n):
        b = int(input())
        if b in pos:
            check[pos[b][0]][pos[b][1]] = 1

    ans = check_bingo(check) 
    print("Yes" if ans else "No")


def C():
    from collections import defaultdict
    n, m = map(int, input().split())
    d = defaultdict(set)
    for i in range(m):
        s, c = map(int, input().split())
        d[s].add(c)

    flag = True
    if n > 1:
        if 1 in d.keys():
            if 0 in d[1]:
                flag = False

    for k in d.keys():
        if len(list(d[k])) > 1:
            flag = False

    if flag:
        ans = ""
        for i in range(n):
            if i+1 in d.keys():
                ans += str(list(d[i+1])[0])
            elif n==1:
                ans += "0"
            elif i+1==1:
                ans += "1"
            else:
                ans += "0"
        ans = int(ans)
    else:
        ans = -1
    print(ans)


# def D():

