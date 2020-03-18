import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='', db=4)
redis_conn = redis.Redis(connection_pool=redis_pool)

data = redis_conn.mget(["all_number", "com_number", "mean_price", "mean_unit_price"])
res = {
    "all_number": str(data[0],encoding='utf-8'),
    "com_number": str(data[1],encoding='utf-8'),
    "mean_price": str(data[2],encoding='utf-8'),
    "mean_unit_price": str(data[3],encoding='utf-8')
}