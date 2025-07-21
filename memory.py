import redis
import json
from config import REDIS_URL

r = redis.from_url(REDIS_URL, decode_responses=True)

def get_chat_history(user_id):
    return [json.loads(m) for m in r.lrange(f"chat:{user_id}", 0, -1)]

def save_message(user_id, role, content, max_len=8):
    key = f"chat:{user_id}"
    r.rpush(key, json.dumps({"role": role, "content": content}))
    r.ltrim(key, -max_len, -1)
