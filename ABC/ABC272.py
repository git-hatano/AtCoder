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
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a))


def B():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]

    for i in range(m):
        a = list(map(int, input().split()))
        for j in range(len(a)):
            if j>0:
                num = a[j]
                g[num-1] += a[1:]
        
    ans = True
    for i in range(n):
        if len(set(g[i]))!=n: 
            ans = False
            break
    print("Yes" if ans else "No")


def C():
    n = int(input())
    a = list(map(int, input().split()))

    if n==2 and sum(a)%2==1:
        ans = -1
    else:
        a = sorted(a, reverse=True)
        tmp_x = 0
        cnt = 0
        for i in range(n):
            if a[i]%2==0:
                tmp_x += a[i]
                cnt +=1
            if cnt==2:
                break
            
        tmp_y = 0
        cnt = 0
        for i in range(n):
            if a[i]%2==1:
                tmp_y += a[i]
                cnt +=1
            if cnt==2:
                break
        ans = max(tmp_x, tmp_y)
        
    print(ans)


def D_WA():
    import math
    n, m = map(int, input().split())
    root_m = math.sqrt(m)
    r = min(n//2+1, int(root_m)+1)

    g = [[-1]*n for _ in range(n)]
    g[0][0] = 0

    for i in range(n):
        for j in range(n):
            if g[i][j]>=0:
                for k in range(-r, r+1):
                    for l in range(-r, r+1):
                        tmp_i = i+k
                        tmp_j = j+l
                        
                        if tmp_i>=0 and tmp_i<=(n-1) and tmp_j>=0 and tmp_j<=(n-1):
                            dist = math.sqrt((i-tmp_i)**2 + (j-tmp_j)**2)
                            if root_m==dist:
                                if g[tmp_i][tmp_j]<0:
                                    g[tmp_i][tmp_j] = g[i][j]+1
    for i in range(n):
        print(" ".join([str(x) for x in g[i]]))

