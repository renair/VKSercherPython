import json
import pickle
import vk
from collections import deque

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
	
	def serch(self,start, end):
		api = vk.VKApi()
		viewed = []
		to_serch = deque([start])
		result = [start]
		while len(to_serch) > 0 and len(viewed) < 15000:
			#api.get_friends(id)
			id = to_serch.popleft()
			result.append(id)
			if id not in viewed:
				list = api.get_friends(id)
				print("founded for "+str(id)+"\t#"+str(len(viewed)))
				if end in list:
					print("Yeah found!!!")
					result.append(end)
					return result
				else:
					to_serch.extend(list)
				viewed.append(id)
			else:
				print(str(id)+"already seen")
			result.pop()
		return none
			
	def smart_serch(self, start, end, deep):
		api = vk.VKApi()
		viewed = []
		to_serch = deque([start])
		result = []
		
	
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


"""
#usage function

AMOUNT = 1000

def download_users(id_from, id_to, filename):
	vk = VKApi.VKApi()
	g = graph.Graph()
	amount = id_to - id_from

	try:
		for i in range(id_from,id_to):
			a = vk.get_friends(i)
			for id in a:
				g.add(i,id)
			print(str((i%amount)*100/amount)+"%"+" "*20,end='\r')
		#print(g.toString())
	except KeyboardInterrupt:
		g.toPickle(filename)
		print("Keyboard Interruption!\nFile "+filename+"  saved")

	except Exception:
		g.toPickle(filename)
		print("Exception on "+str(id_from)+" - "+str(id_to))

	print("parsed")
	g.toPickle(filename)
	print("pickled successfull")

"""

#-----Main part------

#for i in range(0,100):
#        print("Downloading "+str(i)+" page")
#        download_users(i*AMOUNT+1,(i+1)*AMOUNT, "dump"+str(i)+".pic")
