# AtCoder
勉強用のリポジトリ

## 📌memo
* Python3よりも、PyPy3の方が速い
* numpyはできるだけ使わない
  * PyPyでは使えない
* 1秒で処理できる計算量は、10^8
* TLEになってからが勝負

## 💡Tips

### 基本的な入力
```
# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))
```

### 初期化
```
# 2次元配列 n*m
dp = [[0]*m for i in range(n)]
```

### リストから先頭要素を削除したいとき
list.pop()は遅いので使わない
```
from collections import deque
x = deque([])
x.append(n)
x.popleft()
```
