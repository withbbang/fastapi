from fastapi import Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from database.connection import set_session_context, reset_session_context, session
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
            session.rollback()
            raise e
        finally:
            session.remove()
            reset_session_context(context=context)

        return response
