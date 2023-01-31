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
    word = "Hello,World!"

    if s==word:
        print("AC")
    else:
        print("WA")


"""
ライブラリを使ったときに、誤差が出るような入力が含まれているのでWAになる
"""
def B_WA():
    n = int(input())

    import math
    k = math.log2(n)
    print(int(k))

def B():
    k = 0
    while n>0:
        k += 1
        n = n//2
    print(k-1)


def C():
    s, k = input().split()
    k = int(k)

    x = []
    from itertools import permutations
    for p in permutations(s, len(s)):
        # print("".join(p))
        x.append("".join(p))
        
    x = sorted(list(set(x)))
    print(x[k-1])


"""
2重ループでTLE. 答えは合ってそう
"""
def D_TLE():
    import math
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    for k in range(1, m+1):
        ok = True
        for i in range(n):
            if math.gcd(a[i], k)!=1:
                ok = False
                break
        if ok:
            ans.append(k)
    l = len(ans)
    ans.sort()
    print(l)
    for i in range(l):
        print(ans[i])


"""
kになれないものを消していく
エラトステネスの篩の要領
"""
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

def D_ans():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #kの候補
    size = max(max(a), m)
    b = [True]*(size+1)

    #素因数分解してkになれないものを削除
    for i in range(n):
        facts = factorization(a[i]) #素因数分解
        for v in facts:
            if v[0]!=1 and b[v[0]]==True: #一度計算したものは再計算しないようにしないとTLE
                for j in range(v[0], size+1, v[0]): #素数の倍数も消す
                    b[j] = False

    #b[i]=Trueになっているものが答え
    ans = []
    for i in range(1, m+1):
        if b[i]:
            ans.append(i)
    print(len(ans))
    for k in ans:
        print(k)
