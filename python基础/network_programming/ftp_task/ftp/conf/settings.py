# -*- coding: utf-8 -*-

import os.path

_project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER_DB_PATH = os.path.join(_project_path, 'db', 'userdb.ini')

ENCODING = 'utf-8'

MAX_BUFFER_SIZE = 1024

USER_BASE_PATH = os.path.join(_project_path, 'dir', 'home')

BASE_DIR = os.path.join(_project_path, 'dir')

USER_DOWNLOAD_BASE_DIR = os.path.join(_project_path, 'dir', 'downloads')

USER_UPLOAD_BASE_DIR = os.path.join(_project_path, 'dir', 'uploads')

STATUS_CODE  = {
    200 : "Task finished",
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'tests.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
    255 : "Filename doesn't provided",
    256 : "File doesn't exist on server",
    257 : "ready to send file",
    258 : "md5 verification",
    259 : "path doesn't exist on server",
    260 : "path changed",
    261 : "send File line",
    262 : "File has exist on server",
    263 : "Put empty file",
    264 : "Put not null file",
    265 : "Get empty file",
    266 : "Path access permitted or Path not exist",
    267 : "pwd invalid cmd arguments",
    268 : "pwd pass",
    269 : "permitted putting same-name file unless continue situation"

}


