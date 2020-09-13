import redis

client = redis.Redis()

x = client.get("name")

print(x)
