
import os


def list_path(p):
    data = [{
        "name": x.name,
        "is_dir": x.is_dir(),
        "is_file": x.is_file(),
        "path": x.path,
        "size": x.stat().st_size,
        "mtime": x.stat().st_mtime,
        "ctime": x.stat().st_ctime
    } for x in os.scandir(p)]
    return data
