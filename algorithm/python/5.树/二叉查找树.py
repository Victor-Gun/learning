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
		if not T: return T
		if T.lchild == None and T.rchild == None:
			if T.parent.lchild == T: T.parent.lchild = None
			else: T.parent.rchild = None
		elif T.lchild == None:
			T.rchild.parent = T.parent
			if T.parent.lchild == T: T.parent.lchild = T.rchild
			else: T.parent.rchild = T.rchild
		elif T.rchild == None:
			T.lchild.parent = T.parent
			if T.parent.lchild == T: T.parent.lchild = T.lchild
			else: T.parent.rchild = T.lchild
		else:
			ln = T.rchild
			while ln.lchild != None: ln = ln.lchild
			ln.lchild = T.lchild
			T.lchild.parent = ln
			if ln != T.rchild:
				ln.rchild = T.rchild
				T.rchild.parent = ln
				ln.parent.lchild = None
			ln.parent = T.parent
			if T.parent != None:
				if T.parent.lchild == T: T.parent.lchild = ln
				else: T.parent.rchild = ln
			else: T = ln
		return T

	def preTranverse(self, T):
		if T == None: return
		self.preTranverse(T.lchild)
		print(T.node.value, T.parent.node.value if T.parent!=None else '-', T.lchild.node.value if T.lchild!=None else '-', T.rchild.node.value if T.rchild!=None else '-')
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
	print('----------------------------')
	T = T.delete(Node(854)) #66 985 545 177 854 
	T.preTranverse(T)
	