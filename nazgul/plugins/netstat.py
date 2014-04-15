def run(plugin, node):
	for process in node.values["processes"]:
		output = node.execute('netstat -pna')

		process["connections"] = []
