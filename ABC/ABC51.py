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
    k, s = map(int, input().split())
    ans = 0
    for x in range(k+1):
        for y in range(k+1):
            z = s-x-y
            if 0<=z<=k:
                ans += 1
    print(ans)


def C():
    sx, sy, tx, ty = map(int, input().split())
    cnt = 0
    ans = [] #進んだ方向を記録
    cur = [sx, sy] #現在地
    s = set() #使った座標を記録
    s.add((cur[0], cur[1]))
    vec = { #進める方向
        "L": [-1, 0], 
        "U": [0,  1], 
        "R": [1,  0], 
        "D": [0, -1], 
    }
    while cnt<4:
        #ゴールを設定
        if cnt%2==0:
            to = (tx, ty)
        else:
            to = (sx, sy)
        
        #現在地からゴールに向かって近づく方向に移動する
        dist = float("inf")
        for k in vec:
            v = vec[k]
            tmp_nex = (cur[0]+v[0], cur[1]+v[1])
            if tmp_nex not in s:
                tmp_dist = (to[0]-tmp_nex[0])**2 + (to[1]-tmp_nex[1])**2
                if dist > tmp_dist:
                    dist = tmp_dist
                    tmp_k = k
        cur = [cur[0]+vec[tmp_k][0], cur[1]+vec[tmp_k][1]]
        ans.append(tmp_k)
        s.add((cur[0], cur[1]))
        
        #ゴールに着いたら次のゴールに設定するためにスタート地点を削除
        if cur[0]==to[0] and cur[1]==to[1]:
            if cnt%2==0:
                s.remove((sx, sy))
            else:
                s.remove((tx, ty))
            cnt += 1

    ans = "".join([str(x) for x in ans])
    print(ans)


# def D():

