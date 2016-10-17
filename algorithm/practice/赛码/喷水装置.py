# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=1651&konwledgeId=134
>题目描述									
	小赛家有一块草坪，长为20米，宽为2米，妈妈要他给草坪浇水，在草坪上放置半径为Ri的喷水装置，每个喷水装置可以给以它为中心的半径为实数Ri(1＜Ri＜15)的圆形区域浇水。他家有充足的喷水装置i（1＜i＜600)个，并且一定能把草坪全部湿润。你能帮他计算一下，把整个草坪全部湿润，最少需要几个喷水装置。
>输入
	输入第一个数字为喷水装置的个数n，后面n个数字分别为n个喷水装置的半径r，r表示该喷水装置能覆盖的圆的半径。
	喷水装置i的范围为：1＜i＜600，半径的范围为：1＜Ri＜15。
>输出
	输出所用装置的个数。
>样例输入
	5
	2 3.2 4 4.5 6
>样例输出
	2
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
while True:  
	li = raw_input()  
	if not li: break
	n = int(li)
	a = sorted(map(int, raw_input().split()))
	w, l, x = 2, 20, 0
	for i in xrange(0, len(a)):
		w -= a[i]
		l -= a[i]