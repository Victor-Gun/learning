# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=3072&konwledgeId=134
>题目描述									
	某国进行军事演戏，研发一种导弹拦截系统。但是这种导弹拦截系统有一个缺陷：虽然它的第一发炮弹能够到达任意的高度，但是以后每一发炮弹都不能高于等于前一发的高度。某天，雷达捕捉到敌国导弹来袭。由于该系统还在试用阶段，所以只用一套系统，因此有可能不能拦截所有的导弹。请你帮忙选择一套系统，根据测试的导弹数量和每次导弹飞来的高度，计算出最多能拦截导弹的数目。
>输入
	第一行输入测试数据组数N（1<=N<=10）
	接下来一行输入这组测试数据共有多少个导弹m（1<=m<=20）
	接下来行输入导弹依次飞来的高度，所有高度值均是大于0的正整数。
>输出
	输出最多能拦截的导弹数目
>样例输入
	2
	8
	389 207 155 300 299 170 158 65
	3
	88 34 65
>样例输出
	6
	2
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
def lcs(a, b):
	al = len(a)
	bl = len(b)
	#print('\n[0,\t\t0,\t\t' + ',\t\t'.join(map(str, a)) + ']')
	t=[0 for i in xrange(0, al+1)]
	#print('[0,\t\t' + (',\t\t'.join(map(str, t))) + ']')
	for i in xrange(0, bl):
		t2=[0 for m in xrange(0, al+1)]
		for j in xrange(0, al):
			if b[i] == a[j]:
				t2[j+1]=t[j]+1
			elif t[j+1]>t2[j]:
				t2[j+1]=t[j+1]
			else: t2[j+1]=t2[j]
		t=t2[:]
		#print('[' + str(b[i]) + ',\t\t' + (',\t\t'.join(map(str, t))) + ']')
	return t[j+1]

T = int(raw_input())
for it in range(0, T):
	t, a = raw_input(), map(int, raw_input().split())
	print(lcs(a, sorted(a, reverse=True)))