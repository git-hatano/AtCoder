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
ans = True #ans = False
print("Yes" if ans else "No")

# リストの中身を文字列に
ans = " ".join([str(x) for x in a])
'''

def A():
    a, b = map(int, input().split())
    ans = a*b -a -b +1
    print(ans)


def divisor_list(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)  
            if i**2 == num:
                continue
            divisors.append(int(num/i))
    return sorted(divisors)

def B():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i%2==1:
            l = divisor_list(i)
            if len(l)==8:
                ans += 1
    print(ans)


def C():
    s = input()
    k = int(input())
    ans = None
    if s[0]!="1":
        ans = s[0]
    else:
        for i in range(len(s)):
            if i==k: #k文字目まで全て1なら1
                break
            if s[i]!="1":
                ans = s[i]
                break
    if ans==None:
        print(1)
    else:
        print(ans)


# def D():

