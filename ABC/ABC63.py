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

# def A():



# def B():


"""
O(2**100)で全bit探索は流石にTLE
"""
def C_TLE():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(int(input()))

    ans = 0
    for bit in range(2**n):
        bit = bin(bit)[2:].zfill(n)
        tmp = 0
        for i, b in enumerate(bit):
            if b=="1":
                tmp += s[i]
        
        if tmp%10 != 0:
            ans = max(ans, tmp)
    print(ans)


def C():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(int(input()))

    ans = 0
    buf_10 = []
    buf_other = []
    for i in range(n):
        if s[i]%10==0:
            buf_10.append(s[i])
        else:
            buf_other.append(s[i])

    if sum(buf_other)%10 != 0:
        ans = sum(s)
    elif len(buf_other)>0:
        buf_other.sort(reverse=True)
        ans = sum(buf_other[:-1]) + sum(buf_10)
    print(ans)


# def D():

