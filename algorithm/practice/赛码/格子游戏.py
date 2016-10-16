# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=1662&konwledgeId=135
>题目描述									
	有n个格子，从左到右放成一排，编号为1-n。
	共有m次操作，有3种操作类型：
	1.修改一个格子的权值，
	2.求连续一段格子权值和，
	3.求连续一段格子的最大值。
	对于每个2、3操作输出你所求出的结果。
>输入
	输入第一行两个整数，n表示格子个数，m表示操作次数，n和m中间用空格隔开；
	接下来输入n行，每行一个整数表示一个格子的权值
	接下来输入m行，每行有三个整数，中间用空格隔开；第一个是选择的操作类型1-3,第二和第三个整数是操作格子的编号。
>输出
	若执行1操作则无输出
	若执行2和3操作则输出一个整数
>样例输入
	3 3
	7
	8
	9
	2 1 3
	3 1 3
	2 1 2
>样例输出
	24
	9
	15
>时间限制
	C/C++语言：2000MS其它语言：4000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
while True:  
	li = raw_input()  
	if not li: break
	n, m = map(lambda x: int(x), li.split())
	a = []
	for i in xrange(0, n):
		a.append(int(raw_input()))
	for i in xrange(0, m):
		t, s, e = map(lambda x: int(x), raw_input().split())	
		if t == 1:
			a[s-1] = e
		elif t == 2:
			sm = 0
			for j in xrange(s-1, e):
				sm += a[j]
			print(sm)
		elif t == 3:
			c = a[s-1]
			if e-s <= 0:
				print(c)
				continue
			for j in xrange(s, e):
				if a[j]>c:
					c = a[j]
			print(c)
