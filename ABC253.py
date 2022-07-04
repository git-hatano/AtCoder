

from math import radians

def B():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())

    points = []
    for h in range(H):
        for w in range(W):
            if S[h][w]=="o":
                points.append([h, w])

    shift = abs(points[1][0]-points[0][0]) + abs(points[1][1]-points[0][1])
    print(shift)



