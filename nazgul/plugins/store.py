import redis
import json
import time


def run(plugin, node):
	node.values['updated'] = int(time.time())

	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	r.set("server_" + node.values['name'], json.dumps(node.values))
