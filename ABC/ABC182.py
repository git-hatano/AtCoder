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
    a, b = map(int, input().split())
    ans = (2*a+100) - b
    print(ans)


def B():
    n = int(input())
    a = list(map(int, input().split()))

    gcd = -1
    ans = -1
    for i in range(2, max(a)+1):
        gcd_tmp = 0
        for j in range(n):
            if a[j]%i==0:
                gcd_tmp += 1
        if gcd_tmp > gcd:
            ans = i
            gcd = gcd_tmp
    print(ans)


"""
全bit探索
解説は解析っぽく解いてる
"""
def C():
    n = input()
    k = len(n)

    ans = k+1
    for bit in range(2**k):
        bit = bin(bit)[2:].zfill(k)
        tmp = []
        for i in range(k):
            if bit[i]=="1":
                tmp.append(n[i])
        
        if len(tmp)>0:
            tmp = int("".join(tmp))
            if tmp%3==0:
                ans = min(ans, k - len(str(tmp)))

    if ans == k+1:
        ans = -1
    print(ans)


# def D():

