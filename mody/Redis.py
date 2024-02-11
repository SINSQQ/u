import redis
import config

r = redis.StrictRedis(host="monorail.proxy.rlwy.net",port=31189,password="C5k6l4LcGn2aH36H6lIjCKOFI1IoAgB1",decode_responses=True)
code = r.get(f'{config.Bot_id}:code')  
va = code.split(':')
redis_url = f"{va[0]}:{va[1]}:{va[2]}"
address, port, password = redis_url.split(":")

db = redis.StrictRedis(
    host=address,
    port=port,
    password=password,
    decode_responses=True
)