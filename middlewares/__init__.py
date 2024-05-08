from fastapi.middleware import Middleware
from .sqlAlchemyMiddleware import SQLAlchemyMiddleware
from .responseSettingMiddleware import ResponseSettingMiddleware

# 밑에서부터 위 순서로 처리
middlewares = [
    # add others...
    Middleware(ResponseSettingMiddleware),
    Middleware(SQLAlchemyMiddleware),
]
