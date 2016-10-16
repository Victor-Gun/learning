# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=1648&konwledgeId=137
>题目描述								
	给定一个递增序列，a1＜a2＜…＜an。定义这个序列的“最大间隔”为         
	现在要从a2,a3...an-1中删除一个元素，问剩余序列的“最大间隔”最小是多少？
>输入
	第一行，一个正整数n（1＜=n＜=100），序列长度。
	接下来n个小于1000的正整数，表示一个递增序列。
>输出
	一个数d表示从a2,a3...an-1中删除一个元素后“最大间隔”的最小值。
>样例输入
	5
	1 2 3 7 8
>样例输出
	4
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
while True:  
	li = raw_input()  
	if not li: break
	n = int(li)
	a = map(int, raw_input().split())
	if n==1:
		print(0)
		continue
	if n==2:
		print(a[1]-a[0])
	t, m = (a[0], 0)
	for i in xrange(1, n):
		a[i-1], t = (a[i]-t, a[i])
		m = a[i-1] if a[i-1]>m else m 
	t = a[0]
	mi = -1
	for i in xrange(1, n-1):	
		a[i-1], t = (a[i]+t, a[i])
		mi = a[i-1] if mi == -1 or mi>a[i-1] else mi
	print(mi if mi>m else m)
