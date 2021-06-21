#http://ip<hyphen-ip>-<session_jd>-<port>.direct.labs.play-with-docker.com

from flask import Flask
from redis import Redis, RedisError
import socket

redis = Redis(host='redis-server')
app = Flask(__name__)

@app.route('/')
def hello():
    try:
        visits = redis.incr('counter')
    except RedisError:
        visits = "cannot connect to redis server"

    html = '<h2>hello folks</h2>\n' \
                '<b>hostname</b>: {hostname}</br>' \
                '<b>visits</b>: {visits}\n'

    return html.format(hostname=socket.gethostname(), visits=visits)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
