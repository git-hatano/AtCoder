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
    k = n//1000
    if n%1000!=0:
        k += 1
    ans = 1000*k - n
    print(ans)


def B():
    n = int(input())
    d = {"AC":0, "WA":0, "TLE":0, "RE":0}

    for i in range(n):
        s = input()
        d[s] += 1

    for key in ["AC", "WA", "TLE", "RE"]:
        print(f"{key} x {d[key]}")


"""
全bit探索（2次元バージョン）
計算量のオーダーがやけに小さいときは全探索bitを疑う
"""
def C():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]

    ans = 0
    #行を選ぶ
    for bi in range(2**h):
        bi = bin(bi)[2:].zfill(h)
        #列を選ぶ
        for bj in range(2**w):
            bj = bin(bj)[2:].zfill(w)
            
            cnt = 0
            for i in range(h):
                for j in range(w):
                    if bi[i]=="1" and bj[j]=="1":
                        if c[i][j]=="#":
                            cnt += 1
            if cnt == k:
                ans += 1
    print(ans)


# def D():

