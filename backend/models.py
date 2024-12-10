from pydantic import BaseModel


class FileModel(BaseModel):
    name: str
    is_dir: bool
    is_file: bool
    path: str
    size: int
    mtime: float
    ctime: float


class UserModel(BaseModel):
    name: str = ""
    password: str = ""
    path: str = ""
