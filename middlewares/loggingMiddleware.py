from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from utils import Result
from models import ResultBase, ResponseBase


# API 에러 처리 여부에 따른 응답값 설정 미들웨어
class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        request_body = await request.body()

        print(f"request body: {request_body.decode('utf-8')}")

        response = await call_next(request)

        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        print(f"response body: {response_body.decode('utf-8')}")

        # Return the response with the new body iterator
        return Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type,
        )
