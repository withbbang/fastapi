from fastapi.middleware import Middleware
from middlewares.sqlAlchemyMiddleware import SQLAlchemyMiddleware

middlewares = [Middleware(SQLAlchemyMiddleware)]
