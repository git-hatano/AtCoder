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
    a, b = map(int, input().split())
    ans = 32**(a-b)
    print(ans)


def B():
    s = input()
    t = input()
    n = len(s)

    ans = False
    if s==t:
        ans = True
    else:
        buf = []
        for i in range(n):
            if s[i]!=t[i]:
                buf.append(i)
        
        if len(buf)==2:
            if buf[1]-buf[0]==1 and s[buf[0]]==t[buf[1]] and s[buf[1]]==t[buf[0]]:
                ans = True
        
    print("Yes" if ans else "No")


def C():
    n = [x for x in input()]

    ans = 0
    from itertools import combinations
    for i in range(1, len(n)//2+1):
        for c in combinations(n, i):
            # print(c)
            a = "".join(sorted(c, reverse=True))
            
            b = n.copy()
            for x in c:
                b.remove(x)
            b = "".join(sorted(b, reverse=True))
            
            if a[0]=="0" or b[0]=="0":
                break
            else:
                a = int(a)
                b = int(b)
                ans = max(ans, a*b)
    print(ans)


def C_2():
    a = [x for x in input()]
    n = len(a)
    ans = 0

    from itertools import permutations
    for p in permutations(a):
        for i in range(n-1):
            l = "".join(p[:i+1])
            r = "".join(p[i+1:])
            
            if l[0]=="0" or r[0]=="0":
                continue
            
            ans = max(ans, int(l)*int(r))

    print(ans)
    

# def D():

