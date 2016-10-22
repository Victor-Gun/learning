# -*- coding: utf-8 -*-
import re
_BLOCK_SIZE_ = 10
def bn_add(a, b):
	pt = re.compile(r'.{1,%s}' % _BLOCK_SIZE_)
	a1, a2 = map(lambda x: x[::-1], pt.findall(str(a)[::-1])), map(lambda x: x[::-1], pt.findall(str(b)[::-1]))
	res, carry = '', 0
	a1, a2, l, m = (a1, a2, len(a1), len(a2)) if len(a1)<len(a2) else (a2, a1, len(a2), len(a1))
	for i in xrange(0, l):
		tmp = str(int(a1[i]) + int(a2[i]) + int(carry))
		if len(tmp) <10 and i != m-1: tmp.zfill(_BLOCK_SIZE_)
		print(int(a1[i]), int(a2[i]), int(carry), tmp)
		res, carry = (tmp[-10]+res, tmp[len(tmp)-10]) if len(tmp)>10 else (tmp+res, '0')
	for i in xrange(l, m):
		tmp = str(int(a2[i]) + int(carry))
		if len(tmp) <10 and i != m-1: tmp.zfill(_BLOCK_SIZE_)
		res, carry = tmp + res, '0'
	return res


if __name__ == '__main__':
	print(bn_add(345678, 123456919202939203920))