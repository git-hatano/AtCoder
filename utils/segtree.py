'''
鉄則本8章のコード
更新に使う関数を問題に合わせて書き換える
	RMQ: max
	RSQ: sum
"""

"""
RMQ (Range Maximum Queries) 
https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A58.py
'''
# セグメント木（ここでは書籍とは異なり、pos が 0-indexed になるように実装しています）
class segtree:
	# 要素 dat の初期化を行う（最初は全部ゼロ）
	def __init__(self, n):
		self.size = 1
		while self.size < n:
			self.size *= 2
		self.dat = [ 0 ] * (self.size * 2)
	
	# クエリ 1 に対する処理
	def update(self, pos, x):
		pos += self.size # pos は 0-indexed なので、A[pos] のみに対応するセルの番号は pos + size
		self.dat[pos] = x
		while pos >= 2:
			pos //= 2
			self.dat[pos] = max(self.dat[pos * 2], self.dat[pos * 2 + 1])
	
	# クエリ 2 に対する処理
	# u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
	def query(self, l, r, a, b, u):
		if r <= a or b <= l:
			return -1000000000 # 一切含まれない場合
		if l <= a and b <= r:
			return self.dat[u] # 完全に含まれる場合
		m = (a + b) // 2
		answerl = self.query(l, r, a, m, u * 2)
		answerr = self.query(l, r, m, b, u * 2 + 1)
		return max(answerl, answerr)


"""
RSQ (Range Sum Queries)
https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap08/answer_A59.py
"""
class segtree:
	# 要素 dat の初期化を行う（最初は全部ゼロ）
	def __init__(self, n):
		self.size = 1
		while self.size < n:
			self.size *= 2
		self.dat = [ 0 ] * (self.size * 2)
	
	# クエリ 1 に対する処理
	def update(self, pos, x):
		pos += self.size # pos は 0-indexed なので、A[pos] のみに対応するセルの番号は pos + size
		self.dat[pos] = x
		while pos >= 2:
			pos //= 2
			self.dat[pos] = self.dat[pos * 2] + self.dat[pos * 2 + 1] # 8.8 節から変更した部分
	
	# クエリ 2 に対する処理
	# u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
	def query(self, l, r, a, b, u):
		if r <= a or b <= l:
			return 0 # 8.8 節から変更した部分
		if l <= a and b <= r:
			return self.dat[u]
		m = (a + b) // 2
		answerl = self.query(l, r, a, m, u * 2)
		answerr = self.query(l, r, m, b, u * 2 + 1)
		return answerl + answerr # 8.8 節から変更した部分



if __name__ == "__main__":
	# 入力
	N, Q = map(int, input().split())
	queries = [ list(map(int, input().split())) for i in range(Q) ]

	# クエリの処理
	Z = segtree(N)
	for q in queries:
		tp, *cont = q
		#更新処理
		if tp == 1:
			pos, x = cont
			Z.update(pos - 1, x) # pos は 1-indexed で入力されるので、update 関数の引数は pos - 1 にします
		#ある区間の最大値を求める処理
		if tp == 2:
			l, r = cont
			answer = Z.query(l - 1, r - 1, 0, Z.size, 1) # 0-indexed の実装では、最初のセルに対応する半開区間は [0, size) です
			print(answer)
