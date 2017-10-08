import numpy as np
from collections import OrderedDict

class ml_helpers:

    def __init__(self, redis_client):
        self.redis_client = redis_client


    @property
    def get_all_malwares(self):
        return sorted(self.redis_client.keys('*'))

    def create_matrix(self, vector_name):
        self.all_malwares = [list(eval(self.redis_client.hget(k, vector_name)).values())for k in self.get_all_malwares]
        return np.array(self.all_malwares)

    def set_label(self, malware, algo,vector_name, label):
        self.redis_client.hset(malware, '%s_%s' % (algo, vector_name), label)

    def get_max_values(self, all_vector, features):
        all_max = OrderedDict()
        for f in features:
            all_max[f] = max([v[f] for v in all_vector])
        return all_max

