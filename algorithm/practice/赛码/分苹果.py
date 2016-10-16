# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=1654&konwledgeId=134
>题目描述							
	果园里有堆苹果，N（1＜N＜9）只熊来分。第一只熊把这堆苹果平均分为N份，多了一个，它把多的一个扔了，拿走了一份。第二只熊把剩下的苹果又平均分成N份，又多了一个，它同样把多的一个扔了，拿走了一份，第三、第四直到第N只熊都是这么做的，问果园里原来最少有多少个苹果？
>输入
	输入1个整数，表示熊的个数。它的值大于1并且小于9。
>输出
	为1个数字，表示果园里原来有的苹果个数。
>样例输入
	5
>样例输出
	3121
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
import math
while True:
	li=raw_input()
	if not li: break
	n=float(li)
	s=n
	while True:
		s1, f, c=(s, True, n)
		while c:
			t=(s1-1)*(n-1)/n
			if math.ceil(t)!=t:
				f=False
				break
			s1, c=(t, c-1)
		if f:
			print(int(s))
			break
		s+=1
'''
打表
a={2:3, 3:25, 4:253, 5:3121, 6:46651, 7:823537, 8:16777209}
while True:
	li=raw_input()
	if not li: break
	print(a[int(li)])
'''