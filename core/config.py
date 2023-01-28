from pydantic import AnyHttpUrl
from typing import List
import os

ENV = os.environ.get("fast_env", "DEV")  # 本次启动环境


class Config:
    APP_NAME = "FastAPI Admin"
    # api前缀
    API_PREFIX = "/api"
    # 跨域白名单
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:8080"]
    # db配置
    DB_URL = ""
    # 启动端口配置
    PORT = 5173
    # 是否热加载
    RELOAD = True


config = Config()