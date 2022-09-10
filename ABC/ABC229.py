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
    s += input()

    ans = True
    if s=="#..#" or s==".##.":
        ans = False

    print("Yes" if ans else "No")


def B():
    a, b = map(int, input().split())
    a = str(a)[::-1]
    b = str(b)[::-1]

    ans = False
    for i in range(min(len(a), len(b))):
        if int(a[i]) + int(b[i]) >= 10:
            ans = True
            break

    print("Hard" if ans else "Easy")


def C():
    n, w = map(int, input().split())
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append([a, b])

    ab = sorted(ab, reverse=True)

    ans = 0
    for i in range(n):
        a = ab[i][0]
        b = ab[i][1]
        
        if w > b:
            ans += a*b
            w -= b
        else:
            ans += a*w
            w = 0
            break        

    print(ans)


def D_TLE():
    s = list(input())
    k = int(input())

    dot_pos = []
    for i, x in enumerate(s):
        if x==".":
            dot_pos.append(i)
    dot_pos = set(dot_pos)

    from itertools import combinations
    ans = 0

    #kが0
    if k==0:
        #連続しているところを探す
        tmp_ans = 0
        cnt = 0
        for i in range(len(s)):
            if s[i]=="X":
                cnt += 1
                if i==len(s)-1:
                    tmp_ans = max(tmp_ans, cnt)
                    
            elif s[i]==".":
                tmp_ans = max(tmp_ans, cnt)
                cnt = 0
        ans = max(ans, tmp_ans)
        
    #1つも"."がないとき、"."がkこより小さいとき
    elif len(dot_pos)==0 or k>=len(dot_pos):
        ans = len(s)
        
    else:
        for c in combinations(dot_pos, k):
            
            buf = []
            # "."を"X"で置き換え
            for i in range(len(s)):
                if i in c:
                    buf.append("X")
                else:
                    buf.append(s[i])
            
            #連続しているところを探す
            tmp_ans = 0
            cnt = 0
            for i in range(len(s)):
                if buf[i]=="X":
                    cnt += 1
                elif buf[i]==".":
                    tmp_ans = max(tmp_ans, cnt)
                    cnt = 0
            ans = max(ans, tmp_ans)
            
    print(ans)


"""
尺取法
"""
def D():
    s = list(input())
    k = int(input())

    #sを01に置き換え
    n = len(s)
    a = []
    for i in range(n):
        a.append(s[i]==".")

    #l:左端、r:右端
    ans = 0
    r = 0
    sum = 0
    #rが左に戻らないから、O(n)
    for l in range(n):
        while r<n and sum+a[r]<=k:
            sum += a[r]
            r += 1
        ans = max(ans, r-l)
        sum -= a[l]

    print(ans)
