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



def C_WA():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ok = False

    a = [[False]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if s[j]=="?" or s[j]==t[i]:
                a[i][j] = True

    for j in range(n):
        if a[0][j]==True:
            ok = True
            for i in range(1, m):
                if j+i<n and a[i][j+i]==True:
                    continue
                else:
                    ok = False
            if ok:
                #ここでbreakしていたのがよくなかった
                #もっと後ろから代入した方が辞書順にしたときにいいやつが見つかる可能性があったから
                start = j
                break 

    if not ok:
        print("UNRESTORABLE")
    else:
        ans = []
        i = 0
        for j in range(n):
            if start<=j<start+m:
                ans.append(t[i])
                i += 1
            elif s[j]=="?":
                ans.append("a")
            else:
                ans.append(s[j])
        ans = "".join([str(x) for x in ans])
        print(ans)


def C():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    #tの各文字がsで入れる場所の候補を探す
    a = [[False]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if s[j]=="?" or s[j]==t[i]:
                a[i][j] = True
    #t全体がsで入れる場所を探す
    start = []
    for j in range(n):
        if a[0][j]==True:
            ok = True
            for i in range(1, m):
                k = j+i
                # print(i, k)
                if k<n and a[i][k]==True:
                    continue
                else:
                    ok = False
            if ok:
                start.append(j)
    #ansの候補を全て求めて、辞書順にソート
    if len(start)==0:
        print("UNRESTORABLE")
    else:
        ans = []
        for st in start:
            tmp = []
            i = 0
            for j in range(n):
                if st<=j<st+m:
                    tmp.append(t[i])
                    i += 1
                elif s[j]=="?":
                    tmp.append("a")
                else:
                    tmp.append(s[j])
            tmp = "".join([str(x) for x in tmp])
            ans.append(tmp)
        ans.sort()
        print(ans[0])


# def D():

