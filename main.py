import vk as VKApi
import graph
import pickle

vk = VKApi.VKApi()
g = graph.Graph()
try:
	for i in range(1,500):
		a = vk.get_friends(i)
		for id in a:
			g.add(i,id)
			
except KeyboardInterrupt:
	vk_dump = g.toJson()
	fi = open('dump.js','w+')
	fi.write(vk_dump)
	fi.flush()
	fi.close()
	print("Keyboard Interruption!\nFile saved")
	exit(0)

except Exception:
	vk_dump = g.toJson()
	fi = open('dump.js','w+')
	fi.write(vk_dump)
	fi.flush()
	fi.close()
	exit(1)

print("parsed")
vk_dump = g.toJson()
fi = open('wwwwwwwwwwwwwww.js','w+')
fi.write(vk_dump)
fi.flush()
fi.close()
g.toPickle("oooooooooooooooooooooooooooo.pic")
