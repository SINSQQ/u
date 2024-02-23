import redis
import config

db = redis.StrictRedis(
    host=config.host,
    port=config.port,
    password=config.password,
    decode_responses=True
)