# -*-coding:utf-8 -*-

import random
class conway(object):
	def __init__(self, row, col, stype):
		self.m_Row = row
		self.m_Col = col
		self.m_Matrix = self.CreateMatrix(stype)
		
	def CreateMatrix(self, stype):
		matrix = []
		for iRow in range(self.m_Row):
			tempLst = []
			for iCol in range(self.m_Col):
				tempLst.append(self.getInitValue(stype))
			matrix.append(tempLst)
		return matrix
		
	def getInitValue(self, stype):
		if stype == "zeros":
			return 0
		elif stype == "random":
			return random.randint(0, 1)
			
	def getDisp(self):
		sResult = ""
		valTostr = {0:" ", 1:"*"}
		for iRow in range(self.m_Row):
			for iCol in range(self.m_Col):
				val = self.m_Matrix[iRow][iCol]
				sResult += valTostr.get(val, " ")
			sResult += "\n"
		return sResult
		
	def printDisp(self):
		print self.getDisp()
		return True
		
	def setPos(self, row, col, val):
		if val not in (0,  1):
			 return False
		
		self.m_Matrix[row][col] = val
		return True
		
	def getNeighbours(self, row, col):
		neighboursLst = []
		for off_row in (-1, 0, 1):
			for off_col in (-1, 0, 1):
				if off_row == 0 and off_col == 0:
					continue
				val = self.m_Matrix[(row+off_row)%self.m_Row][(col+off_col)%self.m_Col]
				neighboursLst.append(val)
		return neighboursLst
		
	def evolve(self, rulefunc):
		if not callable(rulefunc):
			return
			
		nextMatrix = self.CreateMatrix("zeros")
		for iRow in range(self.m_Row):
			for iCol in range(self.m_Col):
				val = self.m_Matrix[iRow][iCol]
				state = rulefunc(val, self.getNeighbours(iRow, iCol))
				nextMatrix[iRow][iCol] = state
		self.m_Matrix = nextMatrix

