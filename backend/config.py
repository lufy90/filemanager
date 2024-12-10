
from fastapi.security import OAuth2PasswordBearer
import os

CWD = os.getcwd()


class AuthConf:
    sec_key = "xxxxxxxxxxxxxx"
    algorithm = "HS256"
    users = [
        {"name": "test", "password": "d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1", "path": ""}
    ]
    schema = OAuth2PasswordBearer(tokenUrl="token")
    expire_min = 60


class RouterConf:
    prefix = "/api"


class PathConf:
    base = "/var/data"
    default = "default"


class AppConf:
    uvicorn = {
        "host": "0.0.0.0",
        "port": 10000,
        "workers": 4,
        "log_config": {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "fuck": {
                    '()': 'uvicorn.logging.AccessFormatter',
                    "fmt": "%(asctime)s %(levelprefix)s %(client_addr)s - '%(request_line)s' %(status_code)s",
                    # "datefmt":"%Y-%m-%d %H:%M:%S"
                },
                "default": {
                    '()': 'uvicorn.logging.DefaultFormatter',
                    'fmt': '%(asctime)s %(levelprefix)s %(message)s',
                }
            },
            "handlers": {
                "access": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "formatter": "fuck",
                    "filename": f"{CWD}/log/filemanager.log",
                    "maxBytes": 1024*1024*5,
                    "backupCount": 3
                },
                "default": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "formatter": "default",
                    "filename": f"{CWD}/log/filemanager.log",
                    "maxBytes": 1024*1024*5,
                    "backupCount": 3
                },
            },
            "loggers": {
                "uvicorn.access": {
                    "handlers": ["access"],
                    "level": "INFO",
                },
                "uvicorn": {
                    "handlers": ["default"],
                    "level": "INFO",
                },
                "uvicorn.error": {
                    "handlers": ["default"],
                    "level": "INFO",
                },
            },
        }
    }
