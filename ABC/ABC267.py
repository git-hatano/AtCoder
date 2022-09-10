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
    d = {"Monday":5, "Tuesday":4, "Wednesday":3, "Thursday":2, "Friday":1}
    print(d[s])

def B():
    s = input()
    s = [int(x) for x in s]

    ans = False
    if s[0]==0:
        pos = [
            sum([s[6]]),
            sum([s[3]]),
            sum([s[1], s[7]]),
            sum([s[0], s[4]]),
            sum([s[2], s[8]]),
            sum([s[5]]),
            sum([s[9]])
        ]
        start = -1
        mid = -1
        end = -1
        for i in range(len(pos)):
            if start<0 and pos[i]==1:
                start = i
            elif start>=0 and pos[i]==0:
                mid = i
            elif start>=0 and mid>0 and pos[i]==1:
                end = i
                ans = True
                break

    print("Yes" if ans else "No")


def C_TLE():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n-m+1):
        tmp = 0
        for j in range(m):
            tmp += (j+1)*a[i+j]
            
        if i==0:
            ans = tmp
        else:
            ans = max(ans, tmp)

    print(ans)
    

def C():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    from itertools import accumulate
    s = [0]+list(accumulate(a))

    sumi = [0]*(n-m+1)
    now = 0
    for i in range(m):
        now += a[i]*(i+1)

    sumi[0] = now

    for i in range(1, n-m+1):
        sumi[i] = sumi[i-1] + m*a[m+i-1] - (s[m+i-1] - s[i-1])

    print(max(sumi))
    



