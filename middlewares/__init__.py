from fastapi.middleware import Middleware
from .sqlAlchemyMiddleware import SQLAlchemyMiddleware

# add others...

middlewares = [Middleware(SQLAlchemyMiddleware)]
