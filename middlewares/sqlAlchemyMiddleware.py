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
        session_id = str(uuid4())
        context = set_session_context(session_id=session_id)

        try:
            response = await call_next(request)
        except Exception as e:
            async with sessionmanager.session() as session:
                await session.rollback()
            raise e
        finally:
            async with sessionmanager.session() as session:
                await session.close()
            reset_session_context(context=context)

        return response
