import time
import bcrypt
import jwt
from fastapi import Header, HTTPException
import config


def hash_pw(p: str) -> str:
    return bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode()


def check_pw(p: str, h: str) -> bool:
    return bcrypt.checkpw(p.encode(), h.encode())


def make_token(uid: int, name: str) -> str:
    return jwt.encode({"id": uid, "name": name, "exp": int(time.time()) + 7 * 86400}, config.JWT_SECRET, algorithm="HS256")


def current_user(authorization: str = Header(default="")):
    try:
        return jwt.decode(authorization[7:], config.JWT_SECRET, algorithms=["HS256"])
    except Exception:
        raise HTTPException(401, "Please sign in again")
