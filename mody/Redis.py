import redis
import config

address, port, password = config.redis_url.split(":")

db = redis.StrictRedis(
    host=address,
    port=port,
    password=password,
    decode_responses=True
)