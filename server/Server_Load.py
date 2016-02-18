# coding: utf-8
from server import *
import os
import traceback
import pickle
try:
	pickle.load(open(os.path.join("resources", "save.p"), 'rb'))
except:
	traceback.print_exc()
	os.mkdir("resources")
	pickle.dump("", open(os.path.join("resources", "save.p"), 'wb'))
main = Engine("")
main.load(pickle.load(open(os.path.join("resources", "save.p"), 'rb')))
print main.map.map
