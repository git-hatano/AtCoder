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
    n,k= map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        del a[0]
        a.append(0)
    ans = " ".join([str(x) for x in a])
    print(ans)


def B():
    import sys
    h, m = map(int, input().split())
    for i in range(24+1):
        for j in range(60):
            if 60*i+j >= 60*h+m:
                si = str(i).zfill(2)
                sj = str(j).zfill(2)
                rh = int(si[0]+sj[0])
                rm = int(si[1]+sj[1])
                if 0<=rh<=23 and 0<=rm<=59:
                    ans = f"{i%24} {j}"
                    print(ans)
                    sys.exit()


def C():
    from collections import defaultdict
    n, q = map(int, input().split())
    d = defaultdict(set)
    for i in range(q):
        t, a, b = map(int, input().split())
        if t==1:
            d[a].add(b)
        if t==2:
            if a in d:
                if b in d[a]:
                    d[a].remove(b)
        if t==3:
            ans = True
            if a not in d[b]:
                ans = False
            if b not in d[a]:
                ans = False
            print("Yes" if ans else "No")


def D_TLE():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    for i in range(q):
        query = list(map(int, input().split()))
        if query[0]==1:
            x = query[1]
            a = [x]*n##TLEになる?
        elif query[0]==2:
            j = query[1]-1
            x = query[2]
            a[j] += x
        elif query[0]==3:
            j = query[1]-1
            print(a[j])


"""
query=1 (reset) を高速化できるかどうか
"""
def D():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    flag_q1 = False
    base = 0
    reseted = set()
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0]==1:
            x = query[1]
            flag_q1 = True
            base = x
            reseted = set()
        elif query[0]==2:
            j = query[1]-1
            x = query[2]
            if flag_q1==False:
                a[j] += x
            else:
                if j not in reseted:
                    a[j] = base+x
                    reseted.add(j)
                else:
                    a[j] += x
        elif query[0]==3:
            j = query[1]-1
            if flag_q1:
                if j in reseted:
                    print(a[j])
                else:
                    print(base)
            else:
                print(a[j])


"""
増加分のみをdictで管理
こっちの方が綺麗
"""
def D_ans():
    from collections import defaultdict
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    base = 0
    add = defaultdict(int)
    for i in range(n):
        add[i] += a[i]

    for qi in range(q):
        query = list(map(int, input().split()))
        if query[0]==1:
            x = query[1]
            base = x
            add = defaultdict(int)
        elif query[0]==2:
            i = query[1]-1
            x = query[2]
            add[i] += x
        elif query[0]==3:
            i = query[1]-1
            ans = base + add[i]
            print(ans)


"""
4重ループを無くせるかどうか
差分を管理するればいいのかな？
"""
def E_TLE():
    H, W, N, h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    #フィルタ動かす用
    for k in range(0, H-h+1):
        buf = []
        for l in range(0, W-w+1):
            #画素見る用
            a_set = set()
            for i in range(H):
                for j in range(W):
                    if not(k<=i<k+h and l<=j<l+w):
                        a_set.add(a[i][j])
            buf.append(len(list(a_set)))
        ans.append(buf)

    for i in range(H-h+1):
        print(" ".join([str(x) for x in ans[i]]))


"""
フィルタを動かした時の差分を管理
"""
def E_ans():
    H, W, n, h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = [[0]*(W-w+1) for i in range(H-h+1)]
    #フィルタを行方向に移動する
    for si in range(H-h+1):
        cnt = [0]*(n+1)
        now = 0
        
        def add(i, j, val=1):
            global now
            x = a[i][j]
            if cnt[x]==0:
                now += 1
            cnt[x] += val
            if cnt[x]==0:
                now -= 1
        
        def delete(i, j):
            add(i, j, val=-1)
        
        #全部追加
        for i in range(H):
            for j in range(W):
                add(i, j)
        #ある行の左上のフィルタ位置で、w-1列分マスクされるものを消す
        for i in range(h):
            for j in range(w-1):
                delete(si+i, j)
        #フィルタを列方向に移動する
        for j in range(W-w+1):
            #フィルタのw列目を消す。解説動画のdel処理
            for i in range(h):
                delete(si+i, w-1+j)
            #今の種類数を保存
            ans[si][j] = now
            #フィルタの0列目を戻す。解説動画のadd処理
            for i in range(h):
                add(si+i, j)
    #output
    for i in range(H-h+1):
        print(" ".join([str(x) for x in ans[i]]))
