'''
鉄則本9章 A68
Ford-Fulkerson法を用いて最大流量問題を解く問題
'''

#最大フロー用の構造体
class maxflow_edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

"""
深さ優先探索
Fはスタートからposに到達する過程での残余グラフの辺の容量の最小値
帰り値は流したフローの量
"""
def dfs(pos, goal, F, G, used):
    #ゴールに到着: フローを流せる
    if pos == goal: 
        return F
    #探索
    used[pos] = True
    for e in G[pos]:
        #容量が1以上でかつ、まだ訪問していない頂点のみに行く
        if e.cap > 0 and not used[e.to]:
            flow = dfs(e.to, goal, min(F, e.cap), G, used)
            #フローを流せる場合、残余グラフの容量をflowだけ増減
            if flow>=1:
                e.cap -= flow
                G[e.to][e.rev].cap += flow
                return flow
    #全ての辺を探索しても見つからない場合
    return 0


"""
頂点sから頂点tまでの最大フローの総流量を返す
N: 頂点数
edges: 辺のリスト
"""
def maxflow(N, s, t, edges):
    #初期状態の残余グラフを構築
    G = [list() for i in range(N+1)]
    for a, b, c in edges:
        G[a].append(maxflow_edge(b, c, len(G[b])))
        G[b].append(maxflow_edge(a, 0, len(G[a])-1))
    
    INF = 10**10
    total_flow = 0
    while True:
        used = [False]*(N+1)
        F = dfs(s, t, INF, G, used)
        if F > 0:
            total_flow += F
        else:
            break #フローを流せなくなったら終了
    return total_flow



N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 答えを求めて出力
answer = maxflow(N, 1, N, edges)
print(answer)
