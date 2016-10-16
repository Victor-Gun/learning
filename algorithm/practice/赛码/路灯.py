# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=1500&konwledgeId=134
>题目描述								
	V先生有一天工作到很晚，回家的时候要穿过一条长l的笔直的街道，这条街道上有n个路灯。假设这条街起点为0，终点为l，第i个路灯坐标为ai。路灯发光能力以正数d来衡量，其中d表示路灯能够照亮的街道上的点与路灯的最远距离，所有路灯发光能力相同。为了让V先生看清回家的路，路灯必须照亮整条街道，又为了节省电力希望找到最小的d是多少？
>输入
	输入两行数据，第一行是两个整数：路灯数目n (1≤n≤1000)，街道长度l (1 ≤l≤109)。第二行有n个整数ai (0 ≤ ai≤ l)，表示路灯坐标，多个路灯可以在同一个点，也可以安放在终点位置。
>输出
	输出能够照亮整个街道的最小d，保留两位小数。
>样例输入
	7 15
	15 5 3 7 9 14 0
>样例输出
	2.50
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
# encoding=utf8

def b(s, e, a, l):
	if e == s: return s
	m = (e-s)/2 + s
	return b(s, m, a, l) if is_cool(a, l, m) else b(m+1, e, a, l)

def is_cool(a, l, m):
	if a[0] > m: return False
	al = len(a)
	if al==1 and l-a[0]>m: return False
	if al==1: return True
	if l-a[al-1]>m: return False
	for i in xrange(1, al):
		if a[i]-a[i-1] > 2*m: return False
	return True

if __name__ == "__main__":
	while True:  
		li = raw_input()  
		if not li: break
		n, l = li.split()
		n, l = (int(n), int(l) * 100)
		a = sorted(map(lambda x: int(x) * 100, raw_input().split()))
		print ('%.2f'%(b(0, l+1, a, l) / 100.0))
