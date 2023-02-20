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
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(m):
        ans += a[b[i]-1]
    print(ans)


def B():
    n, k = map(int, input().split())
    s = input()
    cnt = 0
    t = []
    for i in range(n):
        if cnt<k and s[i]=="o":
            t.append("o")
            cnt += 1
        else:
            t.append("x")
    ans = "".join([str(x) for x in t])
    print(ans)


def C():
    from collections import Counter
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    counter = Counter(a)
    ans = 0
    for i in range(n):
        if ans<k and i in counter:
            ans += 1
        else:
            break
    print(ans)


# def D():
memo = {}
t = int(input())
for _ in range(t):
    n, d, k = map(int, input().split())
    d %= n
    if n not in memo:
        memo[n] = list(range(n))
    
    if k==1:
        print(0)
    else:
        j = (d*(k-1))%n
        if j==0:
            j += 1
        print(memo[n][j])

