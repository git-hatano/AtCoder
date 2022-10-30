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
    if s=="SSS":
        ans = 0
    elif s=="RRR":
        ans = 3
    elif "RR" in s:
        ans = 2
    elif "R" in s:
        ans = 1
    print(ans)


def B():
    from itertools import combinations
    n = int(input())
    l = list(map(int, input().split()))

    ans = 0
    if n>=3:
        for c in combinations(l, 3):
            c = list(set(c))
            if len(c)==3:
                c = sorted(c)
                if c[0]+c[1]>c[2]:
                    ans += 1
    print(ans)


"""
絶対値のつけ忘れ
"""
def C_WA():
    x, k, d = map(int, input().split())
    x = abs(x)

    if x - k*d >= 0:
        ans = x - k*d
    else:
        need_k = x//d
        now_pos = x - need_k*d
        k -= need_k
        
        #もう一歩先の方が0に近かったら更新
        if k>0:
            next_pos = now_pos - d
            if now_pos > abs(next_pos):
                now_pos = next_pos
                k -= 1
        
        if k%2==0:
            ans = now_pos
        else:
            ans = min(abs(now_pos-d), now_pos+d)
        
    print(ans)


def C():
    x, k, d = map(int, input().split())
    x = abs(x)

    if x - k*d >= 0:
        ans = x - k*d
    else:
        need_k = x//d
        now_pos = x - need_k*d
        k -= need_k
        
        #もう一歩先の方が0に近かったら更新
        if k>0:
            next_pos = now_pos - d
            if now_pos > abs(next_pos):
                now_pos = next_pos
                k -= 1
        
        if k%2==0:
            ans = abs(now_pos)
        else:
            ans = min(abs(now_pos-d), abs(now_pos+d))
        
    print(ans)


# def D():

