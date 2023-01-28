import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
from core.config import config
from apis.apis import api_router

app = FastAPI(
    title="FastAPI Admin API Docs",
    description="项目代码： https://github.com/ueumd/fastapi-admin",
    version='1.0.0',
    docs_url='/docs'
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in config.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求头
@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['token'] = str(process_time)
    return response

# 注册路由
app.include_router(api_router, prefix=config.API_PREFIX)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=config.PORT, reload=config.RELOAD, debug=True, workers=1)