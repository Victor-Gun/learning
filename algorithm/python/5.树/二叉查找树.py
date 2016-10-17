# -*- coding: utf-8 -*-
class Node:
	"""树节点"""
	def __init__(self, value):
		self.value = value

	def cmp(self, node):
		return 1 if self.value>node.value else -1 if self.value<node.value else 0
		
class BSTree:
	def __init__(self):
		self.rchild = None
		self.lchild = None
		self.node = None
	def insert(self, T, node):
		if T.node == None:
			T.node = node
		elif T.node.cmp(node)>0:
			if T.lchild == None: T.lchild = BSTree()
			T.lchild = self.insert(T.lchild, node)
		else:
			if T.rchild == None: T.rchild = BSTree()
			T.rchild = self.insert(T.rchild, node)
		return T

	def delete(self, i):
		pass

	def preTranverse(self, T):
		if T == None: return
		self.preTranverse(T.lchild)
		print(T.node.value)
		self.preTranverse(T.rchild)

if __name__ == "__main__":
	a = [854,545,127,427,769,942,985,984,84,177,261,981,127,422,975,318,66,803,641,845]
	T = BSTree()
	for i in a:
		T = T.insert(T, Node(i))
	T.preTranverse(T)