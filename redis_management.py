from redis import StrictRedis


class RedisManagement:

    def __init__(self, name_of_table, hostname='localhost'):
        self.redis_table = {
            'stats': 0,
            'malwares': 1,
            }
        self.redis_client = StrictRedis(host=hostname, db=self.redis_table[name_of_table])

    def record_vector(self,sha256,name_of_vector,vector_malware):
        self.redis_client.hset(sha256, name_of_vector,vector_malware)