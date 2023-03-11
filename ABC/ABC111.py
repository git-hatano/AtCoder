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
    s = input()
    ans = []
    for c in s:
        if c=="1":
            ans.append("9")
        elif c=="9":
            ans.append("1")
        else:
            ans.append(c)
    ans = "".join([str(x) for x in ans])
    print(ans)


def B():
    n = int(input())
    for i in range(1, 10):
        x = 100*i + 10*i + i
        if x>=n:
            print(x)
            break


def C_WA():
    from collections import Counter
    n = int(input())
    v = list(map(int, input().split()))
    a = [] #偶数用
    b = [] #奇数用
    for i in range(n):
        if i%2==0:
            a.append(v[i])
        else:
            b.append(v[i])
    cnt_a = Counter(a)
    cnt_b = Counter(b)
    keys = set(list(cnt_a.keys()) + list(cnt_b.keys()))
    ans = 0
    if len(keys)>1:
        if len(cnt_a.keys())>1:
            ma = 0
            for k in cnt_a:
                ma = max(ma, cnt_a[k])
            ans += len(a) - ma

        if len(cnt_b.keys())>1:
            ma = 0
            for k in cnt_b:
                ma = max(ma, cnt_b[k])
            ans += len(b) - ma
    else:
        ans = n//2
    print(ans)


"""
Webの情報をそのまま信用しない
辞書のソートはめんどい
"""
def C_ans():
    from collections import defaultdict
    n = int(input())
    v = list(map(int, input().split()))
    cnt_a = defaultdict(int) #偶数用
    cnt_b = defaultdict(int) #奇数用
    for i in range(n):
        if i%2==0:
            cnt_a[v[i]] += 1
        else:
            cnt_b[v[i]] += 1

    keys_a = sorted(cnt_a.items(), key=lambda x: x[1], reverse=True)
    keys_b = sorted(cnt_b.items(), key=lambda x: x[1], reverse=True)
    #どちらも最適
    if keys_a[0][0]!=keys_b[0][0]:
        ans = n - cnt_a[keys_a[0][0]] - cnt_b[keys_b[0][0]]
    #すべて同じ数
    elif len(keys_a)==1 or len(keys_b)==1: 
        ans = n//2
    #どちらかを妥協する、どっちを妥協するのが最適かはどちらも試してより良い方を採用
    else:
        ans = 10**9
        if len(keys_a)>1:
            ans = min(ans, n - cnt_a[keys_a[1][0]] - cnt_b[keys_b[0][0]])
        if len(keys_b)>1:
            ans = min(ans, n - cnt_a[keys_a[0][0]] - cnt_b[keys_b[1][0]])
    print(ans)
