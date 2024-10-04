# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
T = int(input())
for _ in range(T):
	x,y,n = map(int, input().split())
	if (x+y)%2 != n%2 or abs(x)+abs(y) > n:
		print('NO')
	else:
		print('YES')	
	
