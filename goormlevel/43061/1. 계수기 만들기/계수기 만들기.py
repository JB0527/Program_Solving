m = int(input())
line_maxs = [v + 1 for v in map(int, input().split())]
line_inits = list(map(int, input().split()))
answers = [0] * m 
count = int(input())

for a, b in zip(line_maxs, line_inits): 
	if a <= b: # 최대값보다 큰 초기값일 경우 -1
		print(-1)
		break
else:
	for i in range(m-1, -1, -1):
		count, answers[i] = divmod((line_inits[i] + count), line_maxs[i])

	print(''.join(map(str, answers)))
