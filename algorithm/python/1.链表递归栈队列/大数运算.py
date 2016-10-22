# -*- coding: utf-8 -*-
import re
_BLOCK_SIZE_ = 10

# 大数加，将字符串倒序后，十个字符一组将字符串分割，把分割好的数组再倒序，保证低位在前
# 以较短的数组为基准，循环相加
# 注意事项：除了最高位以外，其他的各位相加的时候，需要保证结果位数为十位。
def bn_add(a, b):
	pt = re.compile(r'.{1,%s}' % _BLOCK_SIZE_)
	a1, a2 = map(lambda x: x[::-1], pt.findall(str(a)[::-1])), map(lambda x: x[::-1], pt.findall(str(b)[::-1]))
	res, carry = '', '0'
	a1, a2, l, m = (a1, a2, len(a1), len(a2)) if len(a1)<len(a2) else (a2, a1, len(a2), len(a1))
	for i in xrange(0, l):
		tmp = str(int(a1[i]) + int(a2[i]) + int(carry))
		if i != m-1 and len(tmp) < _BLOCK_SIZE_: tmp = tmp.zfill(_BLOCK_SIZE_)
		res, carry = (tmp[-_BLOCK_SIZE_]+res, tmp[len(tmp)-_BLOCK_SIZE_]) if len(tmp)>_BLOCK_SIZE_ else (tmp+res, '0')
	for i in xrange(l, m):
		tmp = str(int(a2[i]) + int(carry))
		if i != m-1 and len(tmp) < _BLOCK_SIZE_: tmp = tmp.zfill(_BLOCK_SIZE_)
		res, carry = tmp + res, '0'
	return res

# 大数减法
def bn_minus(a, b):
	a, b = str(a).lstrip('0'), str(b).lstrip('0')
	mFlag, a, b = (False, a, b) if len(a) > len(b) or (len(a) == len(b) and a > b) else (True, b, a)
	pt = re.compile(r'.{1,%s}' % _BLOCK_SIZE_)
	a1, a2 = map(lambda x: x[::-1], pt.findall(str(a)[::-1])), map(lambda x: x[::-1], pt.findall(str(b)[::-1]))
	res, bow, m, l = '', '0', len(a1), len(a2)
	for i in xrange(0, l):
		a1i = int(a1[i]) if int(a1[i]) >= int(a2[i]) + int(bow) else int('1' + a1[i])
		tmp = str(a1i - int(a2[i]) - int(bow))
		if i != m-1 and len(tmp) < _BLOCK_SIZE_: tmp = tmp.zfill(_BLOCK_SIZE_)
		res, bow = (tmp + res), '1' if int(a1[i]) < int(a2[i]) + int(bow) else '0'
		print(a1i, a2[i], bow, tmp, res)
	for i in xrange(l, m):
		a1i = int(a1[i]) if int(a1[i]) >= int(bow) else int('1' + a1[i])
		tmp = str(a1i - int(bow))
		if i != m-1 and len(tmp) < _BLOCK_SIZE_: tmp = tmp.zfill(_BLOCK_SIZE_)
		res, bow = tmp + res, '1' if int(a1[i]) < int(bow) else '0'
	res = '0' if res.lstrip('0') == '' else res.lstrip('0')
	return '-' + res if mFlag else res
	

if __name__ == '__main__':
	print(bn_minus('647406906820834883639534469694', '1292142309248447204926498234272'))
