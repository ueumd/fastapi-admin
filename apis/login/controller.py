from fastapi import APIRouter, Depends, HTTPException, status

login_router = APIRouter()

@login_router.post('/login', name='用户登录')
async def login():
    return 'ok'

@login_router.post("/logout", name="用户登出")
def logout():
    return {"message": "已登出"}