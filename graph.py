import json
import pickle

class Graph:
	
	def __init__(self):
		self.vertex = dict()
	
	def add(self,first,second):
		if not self.vertex.get(first):
			self.vertex[first] = [second]
		elif not second in self.vertex[first]:
			self.vertex[first].append(second)
		if not self.vertex.get(second):
			self.vertex[second] = [first]
		elif not first in self.vertex[second]:
			self.vertex[second].append(first)
	
	def fromPickle(self, filename):
		self.vertex = pickle.load(open(filename,'rb'))
	
	def toPickle(self,filename):
		pickle.dump(self.vertex,open(filename,'wb+'))
	
	def toString(self):
		s = ''
		for key,value in self.vertex.items():
			s += (str(key)+' -> '+str(value)+'\n')
		return s
	def toJson(self):
		return json.dumps(self.vertex)
