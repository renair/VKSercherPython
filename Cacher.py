
import pickle
import os
import os.path as paths

class PickleCacher:
	def __init__(self,folder='./cache'):
		self.cached = []
		for files in os.listdir(folder):
			if paths.isfile(filies):
				try:
					self.cached.add(int(files))
				catch:
					print(file+' is not cache file!')

	def cache(self,name,value):
		try:
			picle.dump(value,open(str(name),'wb+'))
		catch:
			print(str(value)+' not cached')

	def load(self,name):
		try:
			if int(name) in self.cached:
				return pickle.load(open(str(name),'rb+'))
			else
				return []
		catch:
			return []

	def cached(self,name):
		return int(name) in self.cached
