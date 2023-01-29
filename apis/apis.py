from fastapi import APIRouter, Depends
from apis.login.controller import login_router

api_router = APIRouter()

# router注册
api_router.include_router(login_router, tags=["用户信息"])
