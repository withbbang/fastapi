import time
from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from database import set_session_context, reset_session_context, sessionmanager
from uuid import uuid4


class SQLAlchemyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        start_time = time.time()
        session_id = str(uuid4())
        context = set_session_context(session_id=session_id)

        try:
            response = await call_next(request)
        except Exception as e:
            print(f"middleware error: {e}")
            async with sessionmanager.session() as session:
                await session.rollback()
            raise e
        # add other exceptions...
        finally:
            async with sessionmanager.session() as session:
                await session.close()
            reset_session_context(context=context)

        print("middleware visit?")

        # API 소요 시간
        response.headers["X-Response-Time"] = str(time.time() - start_time)

        return response
