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
		self.parent = None
		self.node = None

	def _insert(self, T, node, parent):
		if T.node == None:
			T.node, T.parent = node, parent
		elif T.node.cmp(node)>0:
			if T.lchild == None: T.lchild = BSTree()
			T.lchild = self._insert(T.lchild, node, T)
		else:
			if T.rchild == None: T.rchild = BSTree()
			T.rchild = self._insert(T.rchild, node, T)
		return T

	def insert(self, node):
		return self._insert(self, node, None)

	def find(self, T, node):
		if T == None: return False
		if T.node.cmp(node)>0: return self.find(T.lchild, node)
		elif T.node.cmp(node)<0: return self.find(T.rchild, node)
		else: return T

	def delete(self, node):
		T = self.find(self, node)

	def preTranverse(self, T):
		if T == None: return
		self.preTranverse(T.lchild)
		print(T.node.value, T.parent.node.value if T.parent!=None else '-')
		self.preTranverse(T.rchild)

if __name__ == "__main__":
	a = [854,545,127,427,769,942,985,984,84,177,261,981,127,422,975,318,66,803,641,845]
	T = BSTree()
	for i in a:
		T = T.insert(Node(i))
	print('----------------------------')
	T.preTranverse(T)
	print('----------------------------')
	print(T.find(T, Node(769)).node.value)