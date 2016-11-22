import vk
import graph
import pickle
import VKFinder

g = VKFinder.Finder()	#graph.Graph()
#users = g.serch(30851865,20056802) # 4-th friend with Castle.... mimimimi
#users = g.serch(30851865,35794528) #Nikita
#g.serch(30851865,8627177) #Ihor friend
vk = vk.VKApi()
#users = g.serch(30851865, 6347171)
#users = g.serch(173852943,9774099) #Taya - Yuara Gromovoi
#users = g.serch(30851865, 648509)

f = open('results.txt','w+')

#for i in range(30851866,30855865):
#	users = g.serch(30851865,i)
#	if len(users):
#		users = vk.get_user(users)
#		for user in users:
#       		f.write(user['first_name']+" "+user['last_name']+" -> ")
#		f.write("\n")
#		f.flush()

users = g.serch(30851865,283505314)
#print(users)
#json = vk.get_user(users)
users = vk.get_user(users)
#users.reverse()
for user in users:
	print(user['first_name']+" "+user['last_name'],end=" -> ")
#print("\n"+str(json))
