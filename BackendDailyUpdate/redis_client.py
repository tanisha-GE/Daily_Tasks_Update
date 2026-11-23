import redis

redis_client=redis.Redis(
    host="localhost",
    port=6397,
    db=0,
    decode_responses=True
)

def check_redis_connection():
    return redis_client.ping()