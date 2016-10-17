# -*- coding: utf-8 -*-
#造一个解析器
#单目运算
#双目运算
#三目运算
'''
'''
import re

_KEY = {
	'+' : 'plus_func',
	'-' : 'minus_func',
	'*' : 'times_func',
	'/' : 'div_func',
	'%' : 'mod_func',
}

def plus_func(a, b):
	return int(a) + int(b)

def minus_func(a, b):
	return int(a) - int(b)

def times_func(a, b):
	return int(a) * int(b)

def div_func(a, b):
	return int(a) / int(b)

def mod_func(a, b):
	return int(a) % int(b)

def rpn(text):
	r = 0 #运算结果
	s = [] #栈
	tokens = re.sub('[\s]+', ' ', text).strip().split()

	for i in xrange(0, len(tokens)):
		#print('----', s) 
		if _KEY.has_key(tokens[i]) or _KEY.has_key(s[-1]): s.append(tokens[i])
		else:
			r = tokens[i]
			while True:
				n1, n2, op = s.pop(), r, s.pop()
				#print(s, n1, n2, op) 
				r = eval(_KEY[op])(n1, n2)
				if len(s) == 0 or _KEY.has_key(s[-1]): break
			if len(s) == 0: break
			s.append(r)
	return (r, True) if len(s) == 0 and i == len(tokens)-1 else (r, False)
if __name__ == '__main__':
	text = '''
	+
		* 2 7
	 	/
	  		6
	  		- 4 1 
	'''
	print(rpn(text))