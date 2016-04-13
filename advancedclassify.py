#!/usr/bin/env python
# -*- coding: utf8 -*-



class matchrow:
	def __init__(self,row,allnum=False):
		if allnum:
			self.data = [float(row[i]) for i in range(len(row)-1)]
		else:
			self.data = row[0:len(row) -1]

		self.match = int(row[len(row)-1])

	
def loadmatch(f,allnum=False):
	rows = []
	for line in file(f):
		rows.append(matchrow(line.split(","),allnum))
	return rows


def lineartrain(rows):
	averages = {}
	counts = {}

	for row in rows:

		# 得到坐标点的所属分类
		cl = row.match

		averages.setdefault(cl,[0.0] * len(row.data))
		counts.setdefault(cl,0)

		# 将该坐标点加入averages中
		for i in range(len(row.data)):
			averages[cl][i] += float(row.data[i])
		
		# 记录每个分类中有多少个坐标点
		counts[cl] += 1

	# 将综合除以计数值以求得平均值
	for cl,avg in averages.items():
		for i in range(len(avg)):
			avg[i] /= counts[cl]

	return averages

def dotproduct(v1,v2):
	return sum(v1[i] * v2[i] for i in range(len(v1)))

def dpclassify(point,avgs):
	b = (dotproduct(avgs[1],avg[1]) - dotproduct(avgs[0],avgs[0])) / 2
	y = dotproduct(point,avgs[0]) - dotproduct(point,avgs[1]) + b
	if y > 0:
		return 0
	else:
		return 1

def yesno(v):
	if v == "yes":
		return 1
	elif v == "no":
		return -1
	else:
		return 0

def matchcount(interest1,interest2):
	l1 = interest1.split(":")
	l2 = interest2.split(":")

	x = 0 
	for v in l1:
		if v in l2:
			x += 1
	return x

def rbf(v1,v2,gamma=20):
	dv = [v1[i]-v2[i] for i in range(len(v1))]
	l = veclength(dv)

	return math.e**(-gamma*1)



if __name__ == "__main__":
	agesonly = loadmatch("agesonly.csv",allnum=True)
	matchmaker = loadmatch("matchmaker.csv")
