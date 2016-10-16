# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=1650&konwledgeId=136
>题目描述										
	某大学开学进行军训队列训练，将学生从一开始按顺序依次编号，并排成一行横队，训练的规则如下：从头开始一至二报数，凡报到二的出列剩下的依次向前靠拢，再从头开始进行一至三报数，凡报到三的出列，剩下的依次向前靠拢，继续从头开始进行一至二报数。。。以后每次从头开始轮流进行一至二报数、一至三报数直到剩下的人数不超过三人为止。
>输入
	第一行为组数N，接着为N行学生人数，学生人数不超过5000。
>输出
	输出有N行，分别对应输入的学生人数，每行输出剩下的学生最初的编号，编号之间有一个空格。
>样例输入
	2
	20
	40
>样例输出
	1 7 19
	1 19 37
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
n = int(raw_input())
for i in xrange(0, n):
	c = int(raw_input())
	f = True
	a = [x for x in xrange(1, c+1)]
	while len(a)>3:
		if f: a, f=[a[i-1] for i in xrange(1, len(a)+1) if i%2!=0], False
		else: a, f=[a[i-1] for i in xrange(1, len(a)+1) if i%3!=0], True
	print ' '.join(map(str, a))