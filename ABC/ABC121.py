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
    H, W = map(int, input().split())
    h, w = map(int, input().split())

    ans = H*W - H*w - (W-w)*h
    print(ans)


def B():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        a = list(map(int, input().split()))
        s = 0
        for j in range(m):
            s += a[j]*b[j]
        if s+c > 0:
            ans += 1
    print(ans)


def C():
    n, m = map(int, input().split())
    x = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append([a, b])
    x.sort()

    ans = 0
    for i in range(n):
        if m==0:
            break
        cnt = min(m, x[i][1])
        ans += x[i][0]*cnt
        m -= cnt
    print(ans)


def D_TLE():
    a, b = map(int, input().split())
    for i in range(a+1, b+1):
        a ^= i
    print(a)


def D_WA():
    a, b = map(int, input().split())
    if a==b:
        print(a)
    else:
        cnt = 0
        x = a
        s = set()
        s.add(x)
        for i in range(a+1, 10**9):
            x ^= i
            if x not in s:
                s.add(x)
                cnt += 1
            else:
                break

        if cnt>0:
            c = b//cnt * cnt
            for i in range(c, b+1):
                x ^= i
        print(x)


"""
数学問題（わからん）
https://drken1215.hatenablog.com/entry/2019/03/09/224100
排他的論理和の性質: a^x=b ならば x=a^b
+
実験的に値の変化を確認したら、繰り返されていることに気づいたのでそれを実装した感じ？
"""
def D_ans():
    def oddsolve(a):#奇数の場合は0か1
        return ((a+1)//2)%2

    def solve(a):
        if a%2==1:
            return oddsolve(a)
        else:
            return oddsolve(a+1) ^ (a+1)

    a, b = map(int, input().split())
    ans = solve(b) ^ solve(a-1)
    print(ans)

