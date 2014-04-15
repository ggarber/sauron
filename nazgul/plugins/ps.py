def run(plugin, node):
	for process in node.values["processes"]:
		output = node.execute("ps -ef | grep " + process["regex"] + " | grep -i 'grep ' | awk '{print $2}'")
		lines = output.readlines()

		process["pid"] = int(lines[0]) if len(lines) else -1
		process["running"] = process["pid"] != -1
