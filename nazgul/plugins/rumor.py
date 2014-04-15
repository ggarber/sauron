def run(plugin, node):
	for process in node.values["processes"]:
		if process['name'] == 'rumor':
			output = node.execute("curl -I http://localhost:5551/server/health")
			lines = output.readlines()

			process["running"] = len(lines) and lines[0].startswith('HTTP/1.1 200 OK')
