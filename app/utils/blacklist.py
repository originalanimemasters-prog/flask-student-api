
blacklisted_tokens = set()

def add_token_to_blocklist(jti):
    blacklisted_tokens.add(jti)

def token_in_blocklist_loader(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in blacklisted_tokens
