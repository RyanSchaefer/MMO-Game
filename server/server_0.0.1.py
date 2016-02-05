# coding: utf-8
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
import os
try:
	pickle.load(open(os.path.join("resources", "save.p"), 'rb'))
except:
	#os.mkdir("resources")
	pickle.dump("", open(os.path.join("resources", "save.p"), 'wb'))
class Building(object):
	pass
class Square(object):
	def __init__(self):
		self.items    = []
		self.players  = []
		self.resources= {}
		#needed since the name of the square is its id
		self.type = ""
	def describe(self):
		print "This is a basic description of a square, update it when you make a square."
class Job(object):
	pass
class Group(object):
	pass
class Player(object):
	def __init__(self):
		self.inventory      = {}
		self.health         = 100
		self.carry_capacity = 100
		self.group          = None
class Building(object):
	def __init__(self):
		self.players = []
		self.items = []
	def describe(self):
		print "This is a basic description, update it when you make a building in a square"
class Swamp(Square):
	def __init__(self):
		self.items = []
		self.type = "swamp"
	def describe(self):
		print "You arrive in a bogged area."
		print "There appears to be a great amount of wood in this area, along with an ample water supply"
		print "There are also %s" % "; ".join(self.items)
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
		pickle.dump(self.variables, open(os.path.join("resources", "save.p"), 'wb'))
	def load(self):
		self.variables = pickle.load(open(os.path.join("resources", "save.p"), 'rb'))
	def update_square(self, square):
		pass
main = Engine("hello")
main.save()
# example declaration of square (square id is name): A1 = Swamp()
A1 = Swamp()
A1.items = ["a test", "another test"]
print A1.describe()