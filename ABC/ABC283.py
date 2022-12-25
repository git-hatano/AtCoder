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
    a, b = map(int, input().split())
    print(a**b)


def B():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        querys = list(map(int, input().split()))
        if querys[0]==1:
            a[querys[1]-1] = querys[2]
        else:
            print(a[querys[1]-1])


def C():
    s = input()
    n = len(s)
    ans = 0
    cur = []
    i = 0
    while i<n:
        if i+1<n and s[i]=="0" and s[i+1]=="0":
            cur.append("0")
            cur.append("0")
            ans += 1
            i += 2
        else:
            cur.append(s[i])
            ans += 1
            i += 1
    print(ans)


def D():
    s = list(input())
    n = len(s)
    box = set()#箱
    pos = []#"("の場所
    balls = {}#key番目の(から囲われている文字
    ans = True

    for i in range(n):
        if s[i]=="(":
            pos.append(i)
            balls[i] = []
            continue
        elif s[i].islower():
            if s[i] in box:
                ans = False
                break
            else:
                box.add(s[i])
                if len(pos)>0:
                    balls[pos[-1]].append(s[i])
        else:
            if len(pos)>0:
                for b in balls[pos[-1]]:
                    box.remove(b)
                del balls[pos[-1]]
                del pos[-1]
    print("Yes" if ans else "No")


def E_WA():
    h, w = map(int, input().split())
    a = ["".join(input().split()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            nears = set()
            if j-1>=0:#左
                nears.add(a[i][j-1])
            if j+1<w:#右
                nears.add(a[i][j+1])
            if i+1<h:#下
                nears.add(a[i+1][j])
            if i-1>=0:#上
                nears.add(a[i-1][j])
            
            if a[i][j] not in nears:#孤立か
                x = int(a[i], 2)
                x = bin(~x & 2**w-1)[2:].zfill(w)
                a[i] = x
                
                nears = set()
                if j-1>=0:#左
                    nears.add(a[i][j-1])
                if j+1<w:#右
                    nears.add(a[i][j+1])
                if i+1<h:#下
                    nears.add(a[i+1][j])
                if i-1>=0:#上
                    nears.add(a[i-1][j])
                if a[i][j] not in nears:#孤立か
                    ans = -1
                    break
                else:
                    ans += 1
    print(ans)

