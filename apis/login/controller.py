from fastapi import APIRouter, Depends, HTTPException, status
from core.resp import resp_200

login_router = APIRouter()

@login_router.post('/login', name='用户登录')
async def login():
    return resp_200(data={'username': 'admin'})

@login_router.post("/logout", name="用户登出")
def logout():
  return resp_200(data='', message='已登出')