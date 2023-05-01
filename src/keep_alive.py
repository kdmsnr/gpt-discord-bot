from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/', methods=['GET'])
def home():
    return Response(status=200)

@app.route('/_ah/warmup', methods=['GET'])
def warmup():
    # Handle your warmup logic. Initiate db connection, etc.
    return Response(status=200)

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
