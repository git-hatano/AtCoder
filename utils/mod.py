"""
余り計算ありの演算をまとめたもの
鉄則本5章から抜粋
"""

#累乗計算
def power(a, b, m):
    import math
    p = a
    ans = 1
    for i in range(math.ceil(math.log2(10**9))):#bの範囲で決まる
        wari = 2**i
        if (b//wari)%2 == 1:
            ans = (ans*p)%m 
        p = (p*p)%m
    return ans


#割り算
def division(a, b, m):
    return (a * power(b, m-2, m))%m


#組み合わせnCr
def combination(n, r, m):
    #分子a
    a = 1
    for i in range(1, n+1):
        a = (a*i)%m
    #分母b
    b = 1
    for i in range(1, r+1):
        b = (b*i)%m
    for i in range(1, n-r+1):
        b = (b*i)%m
    return division(a, b, m)


mod = 10**9 +7
n = 4
r = 2
print(combination(n, r, mod)) #6
