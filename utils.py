from json import load
from hashlib import sha256
from string import punctuation


def get_cfg() -> dict or None:
    return load(open('./config.json', 'r+'))


def hs(string: str) -> str:
    return sha256(string.encode('utf-8')).hexdigest()


def valid_password(pw: str) -> dict:
    resp = {
        'valid': True,
        'reason': ''
    }
    if not (8 < len(pw) <= 32):
        resp['valid'] = False
        resp['reason'] = 'Password length less than 8 or more than 32'
    else:
        for char in pw:
            if char in punctuation and char != '.':
                resp['valid'] = False
                resp['reason'] = 'Password contains a restricted character '+char
                break

    return resp
