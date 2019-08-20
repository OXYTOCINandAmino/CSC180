# -*-coding:utf-8 -*-

import random
class conway(object):
	def __init__(self, row, col, stype):
		self.m_Row = row-1
		self.m_Col = col-1
		self.m_Matrix = None
		
		self.Init(stype)
		
	def Init(self, stype):
		self.m_Matrix = []
		for iRow in range(self.m_Row):
			tempLst = []
			for iCol in range(self.m_Col):
				tempLst.append(self.getInitValue(stype))
			self.m_Matrix.append(tempLst)
		
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
			sResult += "/n"
		return sResult
		
	def printDisp(self):
		print self.getDisp()
		return True
		
	def setPos(row, col, val):
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
				val = self.m_Matrix[row+off_row][col+off_col]
				neighboursLst.append(val)
		return neighboursLst
		
