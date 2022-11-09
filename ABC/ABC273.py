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
    def func(x):
        if x==0:
            return 1
        return x*func(x-1)

    n = int(input())
    print(func(n))


"""
参考: https://note.nkmk.me/python-round-decimal-quantize/
"""
def B_WA():
    def my_round(val, digit=0):
        p = 10 ** digit
        out = (val * p * 2 + 1) // 2 / p
        return int(out)

    x, k = map(int, input().split())
    for i in range(k+1):
        x = my_round(x, -i)
    print(x)


def B():
    x, k = map(int, input().split())
    for i in range(k):
        m = x%10**(i+1)
        x //= 10**(i+1)
        x *= 10**(i+1)
        
        if m >= 5*(10**i):
            x += 10**(i+1)
    
    print(x)


def C_TLE():
    n = int(input())
    a = list(map(int, input().split()))

    for k in range(n):
        ans = 0
        for i in range(n):
            buf = set()
            for j in range(n):
                if a[j] > a[i]:
                    buf.add(a[j])
            if len(list(buf)) == k:
                ans += 1
        print(ans)


def C_TLE2():
    n = int(input())
    a = list(map(int, input().split()))
    
    b = sorted(list(set(a)))
    len_b = len(b)
    d = {}
    for i in range(len_b):
        d[b[i]] = len_b - (i+1)
    
    for k in range(n):
        ans = 0
        for i in range(n):
            if d[a[i]] == k:
                ans += 1
        print(ans)


"""
1つのループで済むように、counterとdict型を駆使した
"""
def C():
    from collections import Counter, defaultdict
    n = int(input())
    a = list(map(int, input().split()))

    #aの分布
    counter = Counter(a)

    #予め、各Aiよりも大きな数の個数を求めておく
    #b: key=Ai, value=Aiよりも大きな個数
    b = sorted(list(set(a)))
    len_b = len(b)
    c = {}
    for i in range(len_b):
        c[b[i]] = len_b - (i+1)

    #d: key=k(個数)
    d = defaultdict(int)
    for key in c:
        d[c[key]] += counter[key]

    for k in range(n):
        ans = 0
        if k in d:
            ans = d[k]
        print(ans)


"""
counterとsortだけで十分
"""
def C_ans():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))

    counter = Counter(a)
    l = []
    for key in counter.keys():
        l.append([key, counter[key]])
    l.sort(reverse=True)

    for k in range(n):
        ans = 0
        if k < len(l):
            ans = l[k][1]
        print(ans)


# def D():

