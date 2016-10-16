# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=1649&konwledgeId=134
>题目描述									
	在经济、科技日益发达的今天，人们对时间的把握越来越严格，对于一个一定影响力的公司的高管来说，他可能要将自己的行程提前安排到下个月。对于普通人来说，他也可能将几天之后的安排已经提前做好。
	请设计一个程序计算出今天距离未来的某一天还剩多少天。
	假设今天是2015年10月18日。
>输入
	输入一个日期格式为yyyy-MM-dd，不考虑日期是否小于今天。
>输出
	输出一个数字表示今天（2015年10月18日）距离该日期还剩多少天。
>样例输入
	2015-10-19
>样例输出
	1
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
import datetime
while True:
	li=raw_input()
	if not li: break
	y,m,d = map(int, li.split('-'))
	d1 = datetime.datetime(y,m,d)
	d2 = datetime.datetime(2015,10,18)
	print((d1-d2).days)