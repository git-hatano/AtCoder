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



def B():
    n, t = map(int, input().split())
    ans = 10**9
    for i in range(n):
        ci, ti = map(int, input().split())
        if ti<=t:
            ans = min(ans, ci)
    if ans==10**9:
        print("TLE")
    else:
        print(ans)


"""
ピラミッドの中心座標を全探索
"""
def C_ans():
    import sys
    n = int(input())
    x = [0]*n
    y = [0]*n
    h = [0]*n
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())

    #中心座標を全探索
    for cx in range(101):
        for cy in range(101):
            H = 1
            #ある点でHの候補を求める
            for i in range(n):
                if h[i]>0:
                    H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
            #Hの候補で他の全ての点で成立するかを確認
            ok = True
            for i in range(n):
                if max(H - abs(x[i]-cx) - abs(y[i]-cy), 0) != h[i]:
                    ok = False
            if ok:
                print(f"{cx} {cy} {H}")
                sys.exit()


"""
約数gのうち、N≦M/gを満たす最大のgが答え
"""
def divisor_list(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)  
            if i**2 == num:
                continue
            divisors.append(int(num/i))
    return sorted(divisors) # 昇順にしたいときはソート

def D():
    n, m = map(int, input().split())
    #約数を求める
    facts = divisor_list(m)

    ans = 1
    for g in facts:
        if n <= m//g:
            ans = g
    print(ans)
