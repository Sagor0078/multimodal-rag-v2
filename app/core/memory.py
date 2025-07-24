from app.core.config import REDIS

def store_short_term(user_id: str, msg: str):
    REDIS.lpush(user_id, msg)
    REDIS.ltrim(user_id, 0, 10)  # Keep only latest 10 messages

def get_short_term(user_id: str):
    return list(reversed(REDIS.lrange(user_id, 0, 10)))
