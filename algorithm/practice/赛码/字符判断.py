# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=3075&konwledgeId=134
>题目描述									
	判断字符串b的所有字符是否都在字符串a中出现过，a、b都是可能包含汉字的字符串。b中重复出现的汉字，那么a中也要至少重复相同的次数。汉字使用gbk编码（简单的说，用两个字节表示一个汉字，高字节最高位为1的代表汉字，低字节最高位可以不为1）。
	        int is_include(char *a, char *b); 
	     返回0表示没有都出现过，返回1表示都出现过。 
	请设计一个算法。
>输入
	从标准输入中读取输入内容，文件中的内容如下
	字符串a\n字符串b
>输出
	标准输出中输出0或者1
>样例输入
	aaaabbbcccdddss
	abc
>样例输出
	1
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
while True:  
	flag = False
	a = raw_input()  
	if not a: break
	b = raw_input()
	for i in b:
		if b.count(i)>a.count(i):
			flag = True
			break
	print(0 if flag else 1)
