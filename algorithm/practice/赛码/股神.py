# encoding=utf8
import sys
import math

def valuable(n, offset):
	if n % 2 == 0 :
		return 2 + ((n-2)/2) * ((n-2)/2+1) / 2 - int((n-1)/2) - 1 + offset
	else :
		return 2 + ((n-1)/2) * ((n-1)/2+1) / 2 - int(n/2) - 1

def get_range(n):
	r = math.sqrt(float(n*2.0) + (1/4.0)) - 1/2.0
	i = int(r)
	return (2 * i - 1, 0) if r == i else (2 * (i+1) - 2, n - i * (i+1) / 2)

if __name__ == "__main__":
	while True:  
		line = raw_input()  
		if not line: break  
		n, offset = get_range(int(line))
		print(valuable(n, offset))
