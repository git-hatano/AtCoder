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

# def A():



# def B():



def C():
    from collections import defaultdict, Counter
    n = int(input())
    d = defaultdict(int) #ansの候補を管理
    for i in range(n):
        s = list(input())
        counter = Counter(s) #今の文字列の個数を管理
        if i==0:
            for c in s:
                d[c] += 1
            continue
        for k in d: #ansの候補を更新
            if k in counter:
                d[k] = min(d[k], counter[k])
            else:
                d[k] = -1
    ans = []
    for k in d:
        if d[k]>0:
            for i in range(d[k]):
                ans.append(k)
    if len(ans)>0:
        ans.sort()
        ans = "".join([str(x) for x in ans])
    else:
        ans = "\n"
    print(ans)


# def D():

