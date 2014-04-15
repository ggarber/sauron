from flask import Flask, render_template
import json
import time
import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', servers=servers())

@app.route("/servers")
def servers():
    servers = {}
    keys = r.keys("server_*")
    for key in keys:
        servers[key] = json.loads(r.get(key))

        # Generate some aggregated information that it is more difficult to generate in the HTML template
        processes_ok = len([x for x in servers[key]['processes'] if not x.get('running')]) == 0
        updated_ok = int(time.time()) - servers[key]['updated'] < 60 * 60
        servers[key]['ok'] = processes_ok and updated_ok

    return servers

@app.route("/:server")
def server():
    return render_template('index.html', servers=servers())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
