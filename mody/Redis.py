import redis
import config

redis_url = config.redis_url
address, port, password = redis_url.split(":")

db = redis.StrictRedis(
    host=address,
    port=port,
    password=password,
    decode_responses=True
)