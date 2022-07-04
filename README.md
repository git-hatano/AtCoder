# AtCoder
勉強用のリポジトリ

## 📌 memo
* Python3よりも、PyPy3の方が速い
* numpyはできるだけ使わない
  * PyPyでは使えない
  * スライシングに頼っているとTLEになりがち
* 1秒で処理できる計算量は、10^8
  * 何重ループして良いかの当たりつけができる 

## 💡　Tips
### リストから先頭要素を削除したいとき
list.pop()は遅いので使わない
```
from collections import deque
x = deque([])
x.popleft()
```

