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
    if a<10 and b<10:
        print(a*b)
    else:
        print(-1)


def B():
    n = int(input())
    ans = False
    for i in range(1, 10):
        for j in range(1, 10):
            if n == i*j:
                ans = True
                break
    print("Yes" if ans else "No")


def C_WA():
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

    from itertools import combinations
    n = int(input())
    facts = factorization(n)
    nums = []
    for f in facts:
        for i in range(f[1]):
            nums.append(f[0])

    if len(nums)==1:
        ans = nums[0]-1
    else:
        ans = 10**10
        for c in combinations(nums, len(nums)//2):
            i = sum(c)
            j = n//i
            ans = min(ans, i-1+j-1)
    print(ans)


def C_ans():
    import math
    n = int(input())
    ans = float("inf")

    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            j = n//i
            ans = min(ans, i-1+j-1)
    print(ans)

