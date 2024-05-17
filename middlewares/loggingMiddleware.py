import json
from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


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

        if request_body:
            try:
                request_body_json = json.loads(request_body)
                pretty_request_body = json.dumps(request_body_json, indent=2)
            except json.JSONDecodeError:
                pretty_request_body = request_body.decode("utf-8")

            print(f"Request: {pretty_request_body}")

        response = await call_next(request)

        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        try:
            response_body_json = json.loads(response_body)
            pretty_response_body = json.dumps(response_body_json, indent=2)
        except json.JSONDecodeError:
            pretty_response_body = response_body.decode("utf-8")

        print(f"Response: {pretty_response_body}")

        # Return the response with the new body iterator
        return Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type,
        )
