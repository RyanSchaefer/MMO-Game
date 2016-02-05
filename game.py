"""
players are objects on the map
connect to central server
map squares are randomly generated as biomes
squads are formed w/ certian benefits (free weapons)
tax can be placed on player in squad (handeled by server)
walls of base are upgraded by players moving materials to bases
players must be accepted into squad
deserter penelties
gather and sell resources (cities)
encounters with other players (run / fight w/ chance based on equipment)
map keeps track of where you have visited
kills reward money (how much?)
claim square a.k.a fortresses (upgradable) (requires you to have a decent sized squad before you can)
water is boundries of map
formal battles (squares locked down?) (bonus for fighting?)
"""
import random
import socket
import pickle
class Building(object):
	pass
class Square(object):
	def __init__(self, socket):
		self.players = []
	def add_player(self, player):
		self.players.append(player)
	def remove_player(self, player):
		self.player.remove(player)
	def send_info(self):
		global socket
		socket.send("hi")
class Job(object):
	pass
class Group(object):
	pass
class Person(object):
	pass
class Building(object):
	pass
class Swamp(Square):
	pass
class Desert(Square):
	pass
class Forrest(Square):
	pass
class City(Square):
	pass
class Bank(Building):
	pass
class Fortress(Building):
	pass
class Map(object):
	def generate():
		pass	
class Engine(object):
	def __init__(self, variables):
		self.variables = variables
	def save(self):
		pickle.dump(self.variables, open("save.p", 'wb'))
	def load(self):
		self.variables = pickle.load(open("save.p", 'rb'))
main = Engine("")
main.load()
print main.variables
s = socket.socket()
s.connect(("irc.twitch.tv", 6667))
Swamp = Swamp(s)
Swamp.add_player("me")
print Swamp.players