# coding: utf-8
"""
!@ MAJOR TODO SENDING TO CLIENT!@
!@ OUTGOING REQUESTS FOR COLORED TEXT IN CONSOLE ARE LABELED AS COLOR :: !@
!@ EXAMPLE "::RED:: username ::WHITE:: joins the server"
"""
import random
import socket
import pickle
import os
import console
from time import sleep
#!@ TODO MAKE ITEM / RESOURCE (ITEMS ARE SINGULAR AND RESOURCES ARE MUTLIPLE)
class Resource(object):
	name = None
	def __init__(self, rarity):
		self.amount = None
		self.extract_time = None
		self.rarity = None
class Wood(Resource):
	name = "wood"
class Stone(Resource):
	name = "stone"
class Water(Resource):
	name = "water"
class Sand(Resource):
	name = "sand"
class Item(object):
	def __init__(self):
		#!@ TODO FIX ITEM ID / NAME / AMOUNT
		self.id = 0
		self.amount = 1
		self.name = ""
	def use(self):
		print "this fuction uses the item"
class Square(object):
	def __init__(self):
		self.items    = {}
		self.players  = {}
		self.resources = {}
		self.buildings= {}
		self.moves = {}
		self.pos = None
	def update_moves(self, pos_x, pos_y):
		self.moves = {"left" : str(pos_x - 1) + ":" + str(pos_y), "up_left" : str(pos_x - 1) + ":" + str(pos_y - 1), "down_left" : str(pos_x - 1) + ":" + str(pos_y + 1), "right" : str(pos_x + 1) + ":" + str(pos_y), "up_right" :str(pos_x + 1) + ":" + str(pos_y - 1), "down_right":str(pos_x + 1) + ":" + str(pos_y + 1), "up": str(pos_x) + ":" + str(pos_y - 1), "down": str(pos_x) + ":" + str(pos_y + 1)}
		self.pos = str(pos_x)+ ":" +str(pos_y)
	def describe(self):
		print "This is a basic description of a square, update it when you make a square."
	def extract(self, resource, player):
		if self.resources[resource.name] > 0:
			sleep(resource.extract_time)
			self.resources[resource.name].amount -= 1
	def add_resource(self, type, amount):
		pass 
class Job(object):
	pass
class Group(object):
	pass
class Player(object):
	def __init__(self, name):
		self.name = name
		self.items      = {}
		#!@ todo add more attributes
		self.attributes     = {"health": 100, "carry_capacity": 100, "evade": 0, "perception": 0}
		self.group          = None
		self.moves = {}
class Building(object):
	def __init__(self):
		self.players = {}
		self.items   = {}
	def describe(self):
		print "This is a basic description, update it when you make a building in a square"
class Swamp(Square):
	type = "swamp"
	def describe(self):
		print "You arrive in a bogged area."
		print "There appears to be a great amount of wood in this area, along with an ample water supply"
		print "You notice there are other buildings including %s" % "; ".join(self.buildings.keys())
		print "There are also %s" % "; ".join(self.items.keys())
class Desert(Square):
	type = "desert"
	def describe(self):
		print "You arrive in a sprawling desert."
		print "There appears to be a great amount of sand here, there is an oasis in the middle of the desert."
		print "You notice there are other buildings including %s" % "; ".join(self.buildings.keys())
		print "There are also %s" % "; ".join(self.items.keys())
class Forrest(Square):
	type = "forrest"
	def describe(self):
		print "You arrive in a wooded area."
		print "There appears to be a great amount of wood here, there is an opening in the middle."
		print "You notice there are other buildings including %s" % "; ".join(self.buildings.keys())
		print "There are also %s" % "; ".join(self.items.keys())
class City(Square):
	type = "city"
	def describe(self):
		print "You arrive in a city."
		print "There are spawling skyscrapers where ever you turn."
		print "You notice there are other buildings including %s" % "; ".join(self.buildings.keys())
		print "There are also %s" % "; ".join(self.items.keys())
class Bank(Building):
	pass
class Fortress(Building):
	pass
class Map(object):
	def __init__(self, squares):
		self.map = {}
		self.squares = squares
	def generate(self, size):
		t_size = float(size * size)
		c_size = 0.0
		cycle = 0
		for y in range(1, size + 1):
			for x in range(1, size + 1):
				self.map.update({str(x) + ":" + str(y) : random.choice(self.squares)()})
				self.map[str(x)+":"+str(y)].update_moves(x,y)
				cycle += 1
				c_size += 1
				if cycle >= 10:
					print "Loading (%.2f%%)..." % ((c_size / t_size) * 100)
					console.clear()
					cycle = 0
class Engine(object):
	def __init__(self, map):
		self.map = map
		self.players = {}
	def save(self):
		pickle.dump(self.map, open(os.path.join("resources", "save.p"), 'wb'))
	def load(self, map):
		self.map = map
	def add_item(self, object, items):
		try:
			items[0]
		except:
			print "Items must be a list"
		for item in items:
			object.items.update({item.name: items})
	def add_player(self, square, player):
		square.players.update({player.name: player})
	def remove_player(self, square, player):
		del square.players[player.name]
	def move(self, square, player, direction):
		x, y = square.moves[direction].split(":")
		if (x != 0) and (y != 0):
			move = square.moves[direction]
			self.add_player(self.map.map[move], player)
			self.remove_player(square, player)
			return True
		else:
			return False
	def add_item(self, sqaure, player, item):
		square.players[player.name].inventory.update({item.name: item})
	def use_item(self, square, player, item):
		square.players[player.name].inventory[item.name].use()
		del square.players[player.name].inventory[item.name]
	def spawn_player(self, player):
		square = random.choice(self.map.map.values())
		square.players.update({player.name: player})
		player.pos = square.pos
		self.players.update({player.name: player})
	def destroy_player(self, player):
		del self.players[player.name]
	def player_thread(self):
		self.socket
	def handout_resources(self, map):
		pass
	def handout_items(self, square):
		pass
"""
Run once function
map = Map([Desert, Swamp, City, Forrest])
map.generate(100)
main = Engine(map)
main.save()
"""