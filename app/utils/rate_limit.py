import time
from functools import wraps
from flask import request, jsonify

requests_store = {}

def rate_limit(limit=5, window=60):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            ip = request.remote_addr
            now = time.time()

            user_requests = requests_store.get(ip, [])
            user_requests = [t for t in user_requests if now - t < window]

            if len(user_requests) >= limit:
                return jsonify({"error": "Rate limit exceeded"}), 429

            user_requests.append(now)
            requests_store[ip] = user_requests

            return fn(*args, **kwargs)
        return wrapper
    return decorator
