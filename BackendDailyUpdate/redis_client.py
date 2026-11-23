
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)


def check_redis_connection():
    return redis_client.ping()


def clear_task_cache(username: str):
    keys = redis_client.scan_iter(
        match=f"tasks:{username}:*"
    )

    for key in keys:
        redis_client.delete(key)
