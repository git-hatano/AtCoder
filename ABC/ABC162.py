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
    s = input()
    if "7" in s:
        ans =True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i%3==0:
            continue
        elif i%5==0:
            continue
        else:
            ans += i
    print(ans)


def C():
    import math
    k = int(input())
    ans = 0
    for a in range(1, k+1):
        for b in range(1, k+1):
            for c in range(1, k+1):
                ans += math.gcd(a, math.gcd(b, c))
    print(ans)


def D_TLE():
    from itertools import combinations
    n = int(input())
    s = input()
    ans = 0
    for c in combinations(range(n), 3):
        i, j, k = c[:]
        if j-i!=k-j and len(set([s[i], s[j], s[k]]))==3:
            ans += 1
    print(ans)

"""
2重ループにできたのはOK
1つ目の条件で全通りを数えたかったのはOK
2つ目の条件を除く方法が上手くできない
"""
def D_WA():
    n = int(input())
    s = input()
    r_pos = set()
    g_pos = set()
    b_pos = set()
    for i in range(n):
        if s[i]=="R":
            r_pos.add(i)
        elif s[i]=="G":
            g_pos.add(i)
        elif s[i]=="B":
            b_pos.add(i)
    ans = 0
    used = set()
    for r in r_pos:
        for g in g_pos:
            i = min(r, g)
            j = max(r, g)
            w = abs(j-i)
            #使えない候補
            b1 = i-w
            b2 = j+w
            b3 = n
            if w>1 and w%2==0:
                b3 = (i+j)//2
            
            for b in [b1, b2, b3]:
                if 0<=b<n and b!=r and b!=g:
                    if b not in b_pos:
                        ans += len(b_pos)
                    else:
                        ans += max(0, len(b_pos)-1)
    print(ans)


def D_ans():
    from collections import Counter
    n = int(input())
    s = input()

    #全部異なる: RGBの組数
    cnt = Counter(list(s))
    ans = cnt["R"]*cnt["G"]*cnt["B"]

    # j-i==k-j の組(等間隔な組)を除く
    for j in range(n):
        for i in range(j):
            k = j + (j-i)
            if k<n:
                if s[i]!=s[j] and s[j]!=s[k] and s[k]!=s[i]:
                    ans -= 1
                """
                if s[i]==s[j] or s[j]==s[k] or s[k]==s[i]:
                    continue
                ans -= 1
                """
    print(ans)

