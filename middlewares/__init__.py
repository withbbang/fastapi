from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from .sqlAlchemyMiddleware import SQLAlchemyMiddleware
from .responseSettingMiddleware import ResponseSettingMiddleware
from .loggingMiddleware import LoggingMiddleware

# 밑에서부터 위 순서로 처리
middlewares = [
    # add others...
    Middleware(LoggingMiddleware),
    Middleware(  # API 에러 처리 여부에 따른 응답값 설정 미들웨어
        ResponseSettingMiddleware
    ),
    Middleware(SQLAlchemyMiddleware),  # DB 세션 처리 미들웨어
    Middleware(  # CORS 미들웨어
        CORSMiddleware,
        allow_origins=["http://localhost:8000"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    ),
    Middleware(  # 신뢰 호스트만 API 수신하는 미들웨어
        TrustedHostMiddleware, allowed_hosts=["localhost"]
    ),
]
