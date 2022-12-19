#Gestionar la conexion con la instancia de redis

from redis import Redis

class Connection:

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def connect_to_redis(self):
        r = Redis(self.hostname, self.port, retry_on_timeout=True)
        return r
