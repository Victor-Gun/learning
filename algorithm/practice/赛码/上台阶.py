'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=1668&konwledgeId=136
>题目描述									
	有一楼梯共m级，刚开始时你在第一级，若每次只能跨上一级或二级，要走上第m级，共有多少走法？
	注：规定从一级到一级有0种走法。
>输入
	输入数据首先包含一个整数n(1<=n<=100)，表示测试实例的个数，然后是n行数据，每行包含一个整数m，（1<=m<=40), 表示楼梯的级数。
>输出	
	对于每个测试实例，请输出不同走法的数量。
>样例输入
	2
	2
	3
>样例输出
	1
	2
>时间限制
	C/C++语言：2000MS其它语言：4000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
a = [0 for i in xrange(0, 41)]
a[1] = 1
for i in xrange(2, 41): a[i] = a[i-2]+a[i-1]
T = int(raw_input())  
for i in xrange(0, T):
	m = int(raw_input())
	print(a[m])
