# -*- coding: utf-8 -*-
_NO_EDGE_ = 0
# 适合用稀疏矩阵
def tpsort(g):
	n, inM, q, res = len(g[0]), {}, [], []
	for i in xrange(0, n):
		inM[i] = reduce(lambda a,b: a+b, [x[i] for x in g])
	res = []
	#遍历入度列表，把所有入度为0零的节点加入队列
	[q.append(k) for k, v in inM.items() if v == 0]	
	while len(q) > 0:
		qH = q.pop(0)
		res.append(qH)
		for i in xrange(0, n):
			if G[qH][i] > 0:
				inM[i] -= 1
				if inM[i] == 0: q.append(i)
	
	return res

if __name__ == '__main__':
	'''
	△ ▽

	A ----------> B <-----------F
	|_____________|_____________
	|			  |				|
	|		 _____|_____		|
	|		|			|		|
	|_______▽	 		▽_______|
	▽							▽
	C-----------> D <-----------E
	'''
	G = [
		[_NO_EDGE_, 1, 1, _NO_EDGE_, 1, _NO_EDGE_], 
		[_NO_EDGE_, _NO_EDGE_, 1, _NO_EDGE_, 1, _NO_EDGE_], 
		[_NO_EDGE_, _NO_EDGE_, _NO_EDGE_, 1, _NO_EDGE_, _NO_EDGE_], 
		[_NO_EDGE_, _NO_EDGE_, _NO_EDGE_, _NO_EDGE_, _NO_EDGE_, _NO_EDGE_], 
		[_NO_EDGE_, _NO_EDGE_, _NO_EDGE_, 1, _NO_EDGE_, _NO_EDGE_],
		[_NO_EDGE_, 1, _NO_EDGE_, _NO_EDGE_, _NO_EDGE_, _NO_EDGE_],
	]

	print(tpsort(G))
