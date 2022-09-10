
def A():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)


def B():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = True
    if n < m:
        ans = False
    else:
        for i in range(m):
            if b[i] not in a:
                ans = False
                break
            else:
                a.remove(b[i])

    if ans:
        print("Yes")
    else:
        print("No")


def C():
    n = int(input())
    s = []
    for i in range(n):
        s.append(list(input()))

    v = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1],
    ]

    # ラスタ操作用
    ans = False
    for i in range(n):
        for j in range(n):
            if s[i][j]=="#":
                # 8方向用
                for k in range(len(v)):
                    vi = v[k][0]
                    vj = v[k][1]

                    # ある方向の探索用
                    buf = {"#":0, ".":0}
                    for l in range(6):
                        if i+vi*l>=0 and i+vi*l<n and j+vj*l>=0 and j+vj*l<n:
                            buf[s[i+vi*l][j+vj*l]] += 1
                        else:
                            break
                    
                    if buf["#"]+buf["."]==6 and buf["#"]>=4:
                        ans = True
                        break

    if ans:
        print("Yes")
    else:
        print("No")
