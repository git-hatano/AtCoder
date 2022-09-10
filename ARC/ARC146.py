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

def A_WA():
    n = int(input())
    a = list(map(int, input().split()))

    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n):
        l = len(str(a[i]))
        m = a[i] // 10**(l-1)
        d[a[i]] = m

    d = sorted(d.items(), key=lambda x:x[1], reverse=True)

    ans = int(str(d[0][0]) + str(d[1][0]) + str(d[2][0]))
    print(ans)


def A_TLE():
    n = int(input())
    a = list(map(int, input().split()))

    #先頭要素
    first = sorted(a, key=lambda x:int(str(x)[0]), reverse=True)[0]
    a.remove(first)
    first = str(first)

    from itertools import combinations
    ans = 0
    for c in combinations(a, 2):
        c = sorted(c, key=lambda x:int(str(x)[0]), reverse=True)
        v = int(first + str(c[0]) + str(c[1]))
        
        if v > ans:
            ans = v
            
    print(ans)




n = int(input())
a = list(map(int, input().split()))

# 桁数の確認: 桁数が大きいものから順に採用したい
lens = [0, 0, 0]
import heapq
heapq.heapify(lens)

for i in range(n):
    minima = heapq.heappop(lens)
    max_len = max(minima, len(str(a[i])))
    heapq.heappush(lens, max_len)

# 桁数が全て同じ [3,3,3]
if len(set(lens))==1:
    a = sorted(a, reverse=True)
    ans = int(str(a[0]) + str(a[1]) + str(a[2]))

# [3,3,2], [3,2,2], [3,2,1]
else:
    a = sorted(a, reverse=True)[0:3]
    
    #これだと抜け漏れ
    # a = sorted(a, key=lambda x:int(str(x)[0]), reverse=True)
    # ans = int(str(a[0]) + str(a[1]) + str(a[2]))
    
    #絞った上で全通り試す (len(a)が3なので大丈夫なはず)
    from itertools import permutations
    ans = 0
    for p in permutations(a, 3):
        # print(p)
        x = int(str(p[0]) + str(p[1]) + str(p[2]))
        ans = max(ans, x)

print(ans)
