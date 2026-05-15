from django.core.cache import cache
import random

PREFIX = 'confirmation code'
TTL = 300

def _key(email):
    return f'{PREFIX}:{email}'

def generate_confirm_code(email):
    code = ''.join([str(random.randint(0 , 9 )) for i in range(6)])
    cache.set(_key(email), code , TTL)
    return code

def save_code_to_cache(email , code):
    key = _key(email)
    cache.set(key, code , TTL)

def verifity_confirmation(email , code ):
    key = _key(email)
    stored = cache.get(key)
    if stored and stored == code:
        cache.delete()
        return True
    return False