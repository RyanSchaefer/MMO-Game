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
!@ MAJOR TODO PRINT SHOULD BE REPLACED WITH SEND !@
!@ SHOULD SEND TO CLIENT !@
"""
import random
import socket
import pickle
import os
try:
	pickle.load(open(os.path.join("resources", "save.p"), 'rb'))
except:
	os.mkdir("resources")
	pickle.dump("", open(os.path.join("resources", "save.p"), 'wb'))
class Item(object):
	def __init__(self):
		self.attributes = {}
		self.id = 0
		self.amount = 1
		self.name = ""
class Square(object):
	def __init__(self):
		self.items    = {}
		self.players  = []
		self.resources= {}
		self.buildings= {}
	def describe(self):
		print "This is a basic description of a square, update it when you make a square."
class Job(object):
	pass
class Group(object):
	pass
class Player(object):
	def __init__(self):
		self.items      = {}
		#!@ todo add more attributes
		self.attributes     = {"health": 100, "carry_capacity": 100, "evade": 0, "perception": 0}
		self.group          = None
class Building(object):
	def __init__(self):
		self.players = []
		self.items   = {}
	def describe(self):
		print "This is a basic description, update it when you make a building in a square"
class Swamp(Square):
	type = "swamp"
	def describe(self):
		print "You arrive in a bogged area."
		print "There appears to be a great amount of wood in this area, along with an ample water supply"
		print "There are also %s" % "; ".join(self.items)
class Desert(Square):
	type = "desert"
	def describe(self):
		print "You arrive in a sprawling desert."
		print "There appears to be a great amount of sand here, there is an oasis in the middle of the desert."
		print "There are also %s" % "; ".join(self.items)
class Forrest(Square):
	pass
class City(Square):
	pass
class Bank(Building):
	pass
class Fortress(Building):
	pass
class Map(object):
	def __init__(self, squares):
		self.map = {}
		self.squares = squares
	def generate(self, size):
		for y in range(size):
			for x in range(size):
				self.map.update({str(x+1) + ":" + str(y+1): random.choice(self.squares)})	
class Engine(object):
	def __init__(self, variables):
		self.variables = variables
	def save(self):
		pickle.dump(self.variables, open(os.path.join("resources", "save.p"), 'wb'))
	def load(self):
		self.variables = pickle.load(open(os.path.join("resources", "save.p"), 'rb'))
	def add_item(self, object, items):
		try:
			items[0]
		except:
			print "Items must be a list"
		for item in items:
			object.items.update({item.name: items})