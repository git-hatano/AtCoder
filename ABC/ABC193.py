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
    ans = (1-b/a)*100
    print(ans)


def B():
    n = int(input())
    ans = 10**10
    for i in range(n):
        a, p, x = map(int, input().split())
        if x-a > 0:
            ans = min(ans, p)
    if ans==10**10:
        print(-1)
    else:
        print(ans)


def C():
    import math
    n = int(input())

    pow_list = set([])
    for a in range(2, int(math.sqrt(n))+1):
        for b in range(2, int(math.log2(n))+1):
            if a**b <=n:
                pow_list.add(a**b)
            else:
                break

    ans = n - len(pow_list)
    print(ans)



def f(cnt, k):
    scores = []
    for i in range(1, 10):
        if cnt[i]+1<=k:
            cnt[i] += 1
            tmp = 0
            for j in range(1, 10):
                tmp += j*(10**cnt[j])
            scores.append(tmp)
            cnt[i] -= 1
    return scores

"""
下記の文章を反映できていない
1, 2, …, 9 はそれぞれ、SとTに合計K回までしか出現しない
"""
def D_WA():
    from collections import Counter
    k = int(input())
    s = [int(x) for x in input()[:-1]]
    t = [int(x) for x in input()[:-1]]

    cnt_s = Counter(s)
    cnt_t = Counter(t)

    s_scores = f(cnt_s, k)
    t_scores = f(cnt_t, k)

    win = 0
    cases = len(s_scores)*len(t_scores)
    for i in range(len(s_scores)):
        for j in range(len(t_scores)):
            if s_scores[i]>t_scores[j]:
                win += 1

    ans = win/cases
    print(ans)


#引数sのスコアを返す
def score(x):
    cnt = [0]*10
    for i in range(len(x)):
        cnt[x[i]] += 1
    ans = 0
    for i in range(1, 10):
        ans += i*(10**cnt[i])
    return ans

def D_ans():
    k = int(input())
    s = [int(x) for x in input()[:-1]]
    t = [int(x) for x in input()[:-1]]
    cnt = [k]*10 #出すことができるカードの集合
    #既に場にあるカードは外す
    for i in range(4):
        cnt[s[i]] -= 1
    for i in range(4):
        cnt[t[i]] -= 1

    ans = 0
    #sの#とtの#に異なるものが入るとき
    for i in range(1, 10):
        if cnt[i]==0:
            continue
        for j in range(1, 10):
            if i==j or cnt[j]==0:
                continue
            if score(s+[i]) > score(t+[j]):
                ans += cnt[i]*cnt[j]
    #sの#とtの#に同じものが入るとき
    for i in range(1, 10):
        if cnt[i]<2: #少なくとも残りで2枚以上存在しないとなり得ない
            continue
        if score(s+[i]) > score(t+[i]):
            ans += cnt[i] * (cnt[i]-1)

    n = 9*k-8
    print(ans / n / (n-1))
