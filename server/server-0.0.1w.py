# coding: utf-8
import random
import console
#pos is a dict with x and y coords
class Square (object):
	#resources are number in a dict in square not an object like previous versions
	def __init__(self):
		self.players = {}
		self.pos = {"x": None, "y": None}
		self.items = {}
		self.moves = {}
	def describe(self):
		print "This is a basic description update it when creating a square object"
### MOVE DESCRIPTIONS TO CLIENT SIDE ###
field_description = "There is a field before you with a small amount of water."
class Field(Square):
	def describe(self):
		print field_description
		print "There are also: " % "; ".join([x for x in self.items.keys()])
forrest_description = "There is a forrest before you full of wood and a small amount of water"
class Forrest(Square):
	def describe(self):
		print forrest_description
		print "There are also: " % "; ".join([x for x in self.items.keys()])
city_description = "There is a city before you with debris scattered about."
class City(Square):
	def describe(self):
		print city_description
		print "There are also: " % "; ".join([x for x in self.items.keys()])
######
class Map (object):
	def __init__(self):
		self.map = {}
	def update_moves(self, square, x, y, max, min):
		if x-1 > min:
		#called when adding to the map, when a player is on it it governs where the player can move to
			square.moves.update({"left" : {"x":x-1,"y":y}})
		else:
			square.moves.update({"left" : None})
		if y-1 > min:
			square.moves.update({"down": {"x":x,"y":y-1}})
		else:
			square.moves.update({"down" : None})
		if x-1 > min and y-1 > min:
			square.moves.update({"down_left" : {"x":x-1,"y":y-1}})
		else:
			square.moves.update({"down_left" : None})
		if x + 1 < max:
			square.moves.update({"right": {"x":x + 1,"y": y}})
		else:
			square.moves.update({"right": None})
		if y + 1 < max:
			square.moves.update({"up" : {"x":x,"y":y+1}})
		else:
			square.moves.update({"up" : None})
		if x + 1 < max and y + 1 < max:
			square.moves.update({"up_right" : {"x": x+1, "y": y+1}})
		else:
			square.moves.update({"up_right" : None})
		if x - 1 > min and y + 1 < max:
			square.moves.update({"up_left": {"x":x-1,"y":y+1}})
		else:
			square.moves.update({"up_left" : None})
		if x + 1 < max and y - 1 > min:
			square.moves.update({"down_right": {"x":x+1,"y": y -1}})
		else:
			square.moves.update({"down_right" : None })
	def generate(self, size, types):
		if isinstance(types, list) and isinstance(size, int):
			cycle, c_size = 0.0, 0.0
			for x in range(1, size+1):
				self.map.update({x:{}})
				for y in range(1, size+1):
					self.map[x].update({y: random.choice(types)()})
					self.update_moves( self.map[x][y], x, y, size+1, 0)
					cycle += 1
					c_size += 1
				if cycle >= 10:
					console.clear()
					print "Loading (%.2f%%)..." % ((c_size / (size*size)) * 100)
					cycle = 0
			console.clear()
			print "Map load complete."
		elif not isinstance(types, list):
			print "Generation types must be a list; generate(size, [types])"
		elif not isinstance(size, int):
			print "Generation size must be a int; generate(size, [types])"
		else:
			print "Unknown error."
class Item (object):
	pass
class Player (object):
	def __init__(self, name):
		self.name = name
		self.pos = {"x": None, "y": None}
		self.inv = {}
		self.rank = ""
		# ranks
		"""
		0 = member
		1 = officer, ability to add players to group
		2 = leader, ability to add and delete players
		"""
class Group (object):
	def __init__(self, name):
		self.name = name
		self.members = {}
class Job (object):
	pass
class Engine (object):
	def __init__(self, map):
		self.players = {}
		self.groups = {}
		self.map = map
	def create_player(self, name):
		if isinstance(name, basestring) and name not in self.players.keys():
			player = Player(name)
			self.players.update({player.name: player})
			return True
		else:
			print "Player already exists!"
			return False 
	def del_player(self, name):
		if name in self.players.keys():
			del self.players[name]
			return True
		else:
			print "Player does not exist!"
			return False
	def spawn_player(self, name):
		if isinstance(name, basestring) and name in self.players.keys():
			x = random.randint(1, max(self.map.keys()))
			y = random.randint(1, max(self.map.keys()))
			self.players[name].pos["x"] = x
			self.players[name].pos["y"] = y
			return True
		else:
			print "Player does not exist"
			return False
	def create_group(self, name):
		if isinstance(name, basestring) and name not in self.groups.keys():
			group = Group(name)
			self.groups.update({group.name: group})
			return True
		else:
			print "Group already exists!"
			return False
	def del_group(self, name):
		if name in self.groups.keys():
			del self.groups[name]
			return True
		else:
			print "Group does not exist!"
			return False
	def add_member(self, g_name, p_name):
		if (isinstance(name, basestring) and g_name in self.groups.keys()) and p_name in self.players.keys():
			self.groups[g_name].members.update({p_name: self.players[p_name]})
			self.players[p_name].rank = "0"
			return True
		else:
			print "Could not add member!"
			return False
	def del_member(self, g_name, p_name):
		if g_name in self.groups.keys() and p_name in self.players.keys():
			del self.groups[g_name].memebers[p_name]
			return True
		else:
			print "Could not delete member!"
			return False
	def move(self, name, direction):
		p_square = self.map[self.players[name].pos["x"]][self.players[name].pos["y"]]
		if name in self.players.keys():
			if p_square.moves[direction] != None:
				self.players[name].pos["x"] = p_square.moves[direction]["x"]
				self.players[name].pos["y"] = p_square.moves[direction]["y"]
				return True
			else:
				return False
				print "Invalid move!"
		else:
			print "Player could not be found!"
 			return False
 	def respawn(self, name):
 		self.players[name].inv = {}
 		self.spawn_player(name)
x = Map()
x.generate(1, [Field, City, Forrest])
main = Engine(x.map)
main.create_player("bob")
main.spawn_player("bob")
print main.players["bob"].pos
main.move("bob", "down_left")
print main.players["bob"].pos
