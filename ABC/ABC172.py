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
    a = int(input())
    ans = a + a**2 + a**3
    print(ans)


def B():
    s = input()
    t = input()
    len_s = len(s)

    ans = 0
    for i in range(len_s):
        if s[i] != t[i]:
            ans += 1
    print(ans)

"""
最小時間のものから読んでいけば良い？
この考え方ではできない
"""
def C_WA():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.append(10**9+10)
    b.append(10**9+10)

    time = 0
    i = 0
    j = 0
    while True:
        mi = min(a[i], b[j])
        
        if time+mi <= k:
            time += mi
            
            if a[i]==mi:
                i += 1
            else:
                j += 1
        else:
            break
    ans = i+j
    print(ans)


"""
しゃくとり法
しゃくとり法は英語だと、2-pointers
"""
def D_ans():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    t = 0
    #bをm冊全て読んだとき
    for i in range(m):
        t += b[i]

    j = m
    ans = 0
    #aをi冊読む
    for i in range(n+1):
        #m冊のうち、kを超えている分を諦める: しゃくとり法
        while j>0 and t>k:
            j -= 1
            t -= b[j]
        #諦めてもkを超えてたらbreak
        if t>k:
            break
        #読める冊数を更新
        ans = max(ans, i+j)
        #iがn冊未満なら、a[i]をtに追加
        if i==n:
            break
        t += a[i]
    print(ans)
