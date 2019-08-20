# -*-coding:utf-8 -*-

def rule(state, neighboursLst):
	sum = 0
	for neighbourState in neighboursLst:
		if neighbourState == 1:
			sum += 1

	if sum == 3:
		return 1
	elif sum == 2:
		return state
	else:
		return 0