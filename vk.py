import urllib.request as net
import json

class VKApi:

	def __init__(self):
		print("tested")

	def get_friends(self, user_id):
		data = net.urlopen("https://api.vk.com/method/friends.get?user_id="+str(user_id)).read().decode('utf-8')
		data = json.loads(data)
		try:
			print(str(user_id)+":"+str(len(data["response"])))
			return data["response"]
		except Exception:
			print("https://api.vk.com/method/friends.get?user_id="+str(user_id))
			print(str(user_id)+":"+str(data))
			return []
