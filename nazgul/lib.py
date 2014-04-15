import paramiko


'''
/server_name
    /name
    /addresses = [string]
    /processes
        /@os
        /process_name
            /name
            /pid
            /running
            /connections = [{from,to,count}]
/@internet
'''

class Client(object):
    def __init__(self, settings):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file(settings['key'])
        self.client.connect(settings['host'], username=settings['username'], pkey=key)

    def execute(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout

class Node(object):
    def __init__(self, settings):
        self.client = Client(settings)
        self.values = {}

    def execute(self, command):
        return self.client.execute(command)

    def set(self, path, value):
        self.values[path] = value

    @staticmethod
    def _pprint(obj, prefix):
        if isinstance(obj, dict) and obj.get("name"):
            print prefix + obj["name"]
            for key, val in sorted(obj.items()):
                if isinstance(val, dict):
                    print prefix + "\t" + key
                    Node._pprint(val, prefix + '\t')
                elif isinstance(val, list):
                    print prefix + "\t" + key
                    for item in val:
                        Node._pprint(item, prefix + '\t\t')
                elif key != "name":
                    print prefix + "\t" + key + ": " + str(val)
        else:
            print prefix + str(obj)

    def pprint(self):
        Node._pprint(self.values, '')

