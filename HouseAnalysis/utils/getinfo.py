import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='', db=4)
redis_conn = redis.Redis(connection_pool=redis_pool)

data = redis_conn.mget(["all_number", "com_number", "mean_price", "mean_unit_price"])
for i in data:
    print(i)