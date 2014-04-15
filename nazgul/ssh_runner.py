from lib import Node
import json
import importlib
import socket

config = json.load(open('config.json'))

for name, server in config["servers"].iteritems():
	role = config["roles"][server["role"]]

	node = Node(server)
	node.values = dict(server.items() + { "name": name }.items())
	node.values["addresses"] = [ socket.gethostbyname(server["host"]) ]
	node.values["processes"] = [ dict(config["processes"][x].items() + { "name": x }.items()) for x in role["processes"] ]

	for name, plugin in config["plugins"].iteritems():
		module = importlib.import_module("plugins." + name)
		method = getattr(module, 'run')

		method(plugin, node)

	node.pprint()
