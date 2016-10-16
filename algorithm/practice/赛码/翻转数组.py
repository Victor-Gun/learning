# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=1656&konwledgeId=134
>题目描述									
	给定一个长度为n的整数数组a，元素均不相同，问数组是否存在这样一个片段，只将该片段翻转就可以使整个数组升序排列。其中数组片段[l,r]表示序列a[l], a[l+1], ..., a[r]。原始数组为
	a[1], a[2], ..., a[l-2], a[l-1], a[l], a[l+1], ..., a[r-1], a[r], a[r+1], a[r+2], ..., a[n-1], a[n]，
	将片段[l,r]反序后的数组是
	a[1], a[2], ..., a[l-2], a[l-1], a[r], a[r-1], ..., a[l+1], a[l], a[r+1], a[r+2], ..., a[n-1], a[n]。
>输入
	第一行数据是一个整数：n (1≤n≤105)，表示数组长度。
	第二行数据是n个整数a[1], a[2], ..., a[n] (1≤a[i]≤109)。
>输出
	输出“yes”，如果存在；否则输出“no”，不用输出引号。
>样例输入
	4
	2 1 3 4
>样例输出
	yes
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
if __name__ == "__main__":
	while True:  
		li = raw_input()  
		if not li: break  
		a = raw_input().split()
		l = len(a)
		if l == 1: 
			print('yes')
			continue
		t, f, c, s, e = int(a[0]), True, 0, -1, -1
		for i in xrange(1,len(a)):
			if f and int(a[i])<t:
				c += 1
				f = False
				s = i-1
			if not f and int(a[i])>t:
				c += 1
				f = True
				e = i-1
			t = int(a[i])
		if c>2:
			print('no')
		elif s == 0 and e == -1:
			print('yes')
		elif s == 0:
			if int(a[s]) <= int(a[e+1]):
				print('yes')
			else: print('no')
		elif e == -1:
			if int(a[s-1])<=int(a[l-1]):
				print('yes')
			else: print('no')
		else:
			if int(a[s-1])<=int(a[e]) and int(a[s])<=int(a[e+1]):
				print('yes')
			else: print('no')