from auth import decode_token, get_user
from models import UserModel
from config import AuthConf

from typing import Annotated
from fastapi import Depends, HTTPException


async def user_dep(token: Annotated[str, Depends(AuthConf.schema)]):
    data = decode_token(token)
    name = data.get("name")
    if name and get_user(name):
        return UserModel(name=name)
    else:
        raise HTTPException(
            status_code=401,
            detail="Authentication failed."
        )
