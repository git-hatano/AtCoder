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
    a = list(map(int, input().split()))
    ans = min(a)
    print(ans)


def B():
    n, m, t = map(int, input().split())
    ans = True
    now_n = n
    now_t = 0
    for i in range(m):
        a, b = map(int, input().split())
        now_n -= (a - now_t)
        if now_n <= 0:
            ans = False
            break
        else:
            now_n = min(n, now_n+(b-a))
            now_t = b

    if ans:
        now_n -= (t - now_t)
        if now_n <= 0:
            ans = False
        
    print("Yes" if ans else "No")


"""
難しく考えすぎ
切るのが可能な場所の選択肢はl-1ヶ所なので、そこから11ヶ所選べば良い
"""
def C_ans():
    import math
    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    l = int(input())
    ans = combinations_count(l-1, 11)
    print(ans)


def D():
    n, m = map(int, input().split())
    a = [x-1 for x in list(map(int, input().split()))]
    a = sorted(a)

    #全て白
    if m == 0:
        ans = 1
    #全て青
    elif n == m:
        ans = 0
    else:
        #サイズ
        if a[0]!=0:
            k = a[0]
        else:
            k = 10**9
        for i in range(1, m):
            k = min(k, max(1, a[i]-a[i-1]-1))
        if a[-1]!=(n-1):
            k = min(k, max(1, n-a[-1]-1))
            
        #回数
        ans = 0
        for i in range(m):
            if i==0:
                whites = a[i]
            else:
                whites = a[i] - a[i-1] -1
            ans += whites//k
            if whites%k>0:
                ans += 1
                
        whites = n -a[-1] -1
        ans += whites//k
        if whites%k>0:
            ans += 1
    print(ans)


def D_ans():
    n, m = map(int, input().split())
    a = [x-1 for x in list(map(int, input().split()))]
    a = sorted(a)
    a.append(n) #最後に青を追加することで実装が楽になる

    cur = 0
    s = []
    for i in range(m+1):
        w = a[i] - cur
        if w>0:
            s.append(w)
        cur = a[i]+1
    k = min(s)

    ans = 0
    for w in s:
        ans += (w+k-1)//k #切り上げの書き方
    print(ans)
