import time
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from utils import Result
from models import ResultBase, ResponseBase


# API 에러 처리 여부에 따른 응답값 설정 미들웨어
class ResponseSettingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        start_time = time.time()

        try:
            response = await call_next(request)
        except Exception:
            result = ResultBase()
            result.setResult(**Result.ERROR.value)
            response_base = ResponseBase(result=result, data=None)

            response = JSONResponse(
                response_base.model_dump(),
                status_code=200,
            )
        # add other exceptions...
        finally:
            pass

        # API 소요 시간
        response.headers["X-Response-Time"] = str(time.time() - start_time)

        return response
