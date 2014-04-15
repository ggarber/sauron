sauron
======

Architecture:
   * nazgul process/es collects data from servers based on different plugins (ps, netstat, curl... ) and push it to a redis database
   * saruman website presents that data from redis database in a visual UI

Requirements:
   * REDIS running in localhost with default configuration

Running:
1. Configure the servers and processes to be monitored in nazgul/config.json
2. Launch nazgul periodically (python ssh_runner.sh)
3. Launch the website (python app.py)
4. Open the website in a browser (http://localhost:5000) and move your servers around

