import redis

config = {
    'host': '192.168.0.102',
    'port': 6379,
}

pool = redis.ConnectionPool(**config, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('name', 'Ubuntu')  # 设置 name 对应的值
print(r.get('name'))  # 取出键 name 对应的值


import time

print(time.time())