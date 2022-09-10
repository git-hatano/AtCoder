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

    c = set()
    from itertools import permutations
    for p in permutations(s):
        c.add("".join(p))

    print(len(c))


def B():
    n = int(input())

    from collections import defaultdict
    d = defaultdict(int)

    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        d[a] += 1
        d[b] += 1

    leaf = 0
    node = 0
    for key in d:
        if d[key]==1:
            leaf += 1
        else:
            node += 1

    if node==1 and leaf==(n-1):
        print("Yes")
    else:
        print("No")


def C():
    def solve():
        n, m = map(int, input().split())
        b = []
        for i in range(n):
            b.append([x-1 for x in list(map(int, input().split()))])

        #端を跨いでないか（7列目と1列目が左右に隣り合っていないか）
        for j in range(m-1):
            if b[0][j]%7 > b[0][j+1]%7:
                print("No")
                return

        #1行目の差が全て1になっているか
        for i in range(n):
            for j in range(m-1):
                if (b[0][j+1] - b[0][j])!=1:
                    print("No")
                    return
                
        #列で見たときに差が7になっているか
        for j in range(m):
            for i in range(n-1):
                if (b[i+1][j] - b[i][j])!=7:
                    print("No")
                    return
        print("Yes")

    solve()


def D_TLE():
    n, q = map(int, input().split())

    querys = []
    for j in range(q):
        querys.append(list(map(int, input().split())))

    #電車の繋がりを管理
    trains = [[x] for x in range(n)]
    #電車がどの繋がりに含まれているかを管理
    pos = list(range(n))
    #空いている場所を管理
    trains_free = []

    for j in range(q):
        query = querys[j]
        
        if query[0]==1:
            x = query[1]-1
            y = query[2]-1
            
            trains[pos[x]] = trains[pos[x]] + trains[pos[y]]                
            trains[pos[y]] = []
            trains_free.append(pos[y])
            
            #pos更新
            for i in trains[pos[x]]:
                pos[i] = pos[x]
        
        elif query[0]==2:
            x = query[1]-1
            y = query[2]-1
            
            #空いている場所を探す
            trains_no = trains_free[-1]
            del trains_free[-1]
            
            #分裂場所
            pos_dev = trains[pos[x]].index(x)
                
            #分裂後 前側
            trains[trains_no] = trains[pos[x]][:pos_dev+1]
            #分裂後 後側
            trains[pos[x]] = trains[pos[x]][pos_dev+1:]
            
            #前側のpos更新
            for i in trains[trains_no]:
                pos[i] = trains_no

        else:
            x = query[1]-1
            m = len(trains[pos[x]])
            jm = " ".join([str(x+1) for x in trains[pos[x]]])
            print(f"{m} {jm}")



"""
双方向リスト
"""
def D():
    n, q = map(int, input().split())

    #電車iの前にある電車
    front = [-1]*n
    #電車iの後ろにある電車
    back = [-1]*n

    for qi in range(q):
        query = list(map(int, input().split()))
        
        if query[0]==3:
            x = query[1]-1
            
            ans = []
            #xが含まれる繋がりの先頭に戻る
            while front[x] != -1:
                x = front[x]
            ans.append(x+1)
            
            #先頭から順に繋がりを辿る
            while back[x] != -1:
                x = back[x]
                ans.append(x+1)
            
            m = len(ans)
            ans = " ".join(str(x) for x in ans)
            print(f"{m} {ans}")
        
        else:
            x = query[1]-1
            y = query[2]-1
            
            if query[0]==1:
                back[x] = y
                front[y] = x
            else:
                back[x] = -1
                front[y] = -1
