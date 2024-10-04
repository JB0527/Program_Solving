# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
block_map = [[0]*3000 for _ in range(3000)]
block = str(input())
score = list(map(int,input().split()))

directions = {
	'R' : (1, 0),
	'U' : (0, 1),
	'L' : (-1, 0),
	'D' : (0, -1)
}
start = [1500, 1500]
block_map[start[1]][start[0]] = 1

move = start
move_history = [move]
for i in range(n):
	#score[i]
	direction = directions[block[i:i+1]]
	p = score[i]
	current = [move[0]+direction[0],move[1]+direction[1]]
	if block_map[current[1]][current[0]] > 0:
		while block_map[current[1]][current[0]] > 0 and len(move_history) > 0:
			history = move_history.pop()
			block_map[history[1]][history[0]] = 0
		block_map[history[1]][history[0]] = p
	else:
		block_map[current[1]][current[0]] = p
	move_history.append(current)
	move = current

result = sum([sum(m) for m in block_map])
 
print(result) 