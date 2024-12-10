import jwt
import json
from datetime import datetime, timezone, timedelta
from hashlib import sha256
from config import AuthConf


def gen_token(data, expire_min=AuthConf.expire_min):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_min)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, AuthConf.sec_key, algorithm=AuthConf.algorithm)


def decode_token(token):
    return jwt.decode(token, AuthConf.sec_key, algorithms=[AuthConf.algorithm])


def validate(username, password):
    password = encrypt_password(password)
    for u in AuthConf.users:
        if username == u["name"] and password == u["password"]:
            return True
    return False


def get_user(name):
    for u in AuthConf.users:
        if u["name"] == name:
            return u
    return None


def encrypt_password(password):
    return sha256(password.encode('utf-8')).hexdigest()
