#--coding:utf8--
INT_MAX = 1000000
def dijkstra(G, v0):
	l = len(G[0])
	dist, nodes, cur, s = [G[v0][i] for i in xrange(0, l)], [1 for i in xrange(0, l)], v0, [v0]
	nodes[cur] = 0
	print(dist, nodes)
	while sum(nodes) > 0:
		minI, minV = -1, INT_MAX
		for i in xrange(0, l):
			if i not in s and G[cur][i] > 0 and G[cur][i] <= minV:
				minI, minV = i, G[cur][i]
		dist[minI], cur = dist[minI] if dist[cur] + minV > dist[minI] else dist[cur] + minV, minI
		s.append(cur)
		for i in xrange(0, l):
			if i not in s and G[cur][i] != INT_MAX and G[cur][i] > 0 and dist[cur] + G[cur][i] < dist[i]:
				dist[i] = dist[cur] + G[cur][i]
		nodes[cur] = 0
		print(dist, nodes)
	return dist

if __name__ == '__main__':
	'''
	△ ▽

	A ----10----> B 
	|_____________|_____________
	|			  |				|
	20		 __5__|__10_		30
	|		|			|		|
	|_______▽	 		▽_______|
	▽							▽
	C------30---> D <-----20----E
	'''
	G = [[0, 10, 20, INT_MAX, 30], [INT_MAX, 0, 5, INT_MAX, 10], [INT_MAX, INT_MAX, 0, 30, INT_MAX], [INT_MAX, INT_MAX, INT_MAX, 0, INT_MAX], [INT_MAX, INT_MAX, INT_MAX, 20, 0]]
	print(dijkstra(G, 0))
