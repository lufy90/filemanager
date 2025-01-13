
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
import os

CWD = os.getcwd()


class AuthConf:
    sec_key = "xxxxxxxxxxxxxx"
    algorithm = "HS256"
    users = [
        ## generate password by `echo -n PASSWORD | sha256sum`
        {"name": "test", "password": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08", "path": ""}
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
    middlewares = [
        {
            "middleware": CORSMiddleware,
            "args": {
                "allow_origins": [
                    "http://10.7.13.132:9003",
                    "http://localhost:9001",
                    "http://10.7.13.132:9001",
                    "http://192.168.1.134:9001",
                    "http://192.168.1.134:9003",
                    "http://192.168.1.134:20083",
                    "https://192.168.1.134:20083",
                    "https://192.168.1.134:20084",
                ],
                "allow_credentials": True,
                "allow_methods": ["*"],
                "allow_headers": ["*"],
            }
        },
        #{
        #    "middleware": HTTPSRedirectMiddleware,
        #    "args": {}
        #}
    ]
