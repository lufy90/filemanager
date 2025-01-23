from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
import os
from config import RouterConf, PathConf, AppConf
from auth import validate, gen_token
from models import UserModel
from dependencies import user_dep
from utils import list_path

app = FastAPI(root_path=RouterConf.prefix)

for middleware in AppConf.middlewares:
    app.add_middleware(middleware["middleware"], **middleware["args"])

@app.post("/token")
async def token(formdata: Annotated[OAuth2PasswordRequestForm, Depends()]):
    username = formdata.username
    password = formdata.password
    if validate(username, password):
        u = UserModel(name=username, password=password)
        return {"access_token": gen_token({"name": u.name}), "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Authentication failed.")


@app.get("/files")
async def get_path(user: Annotated[UserModel, Depends(user_dep)], path: str = ""):
    if os.path.isabs(path):
        path = path[1:]
    userpath = user.path
    if not userpath:
        userpath = user.name
    base_path = os.path.join(PathConf.base, userpath)
    real_path = os.path.join(base_path, path)
    resp = map(lambda x:{**x, "path":x["path"][len(base_path):]}, list_path(real_path)) 
    return list(resp)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", **AppConf.uvicorn)
