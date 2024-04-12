from fastapi.middleware import Middleware
from middlewares.sqlAlchemyMiddleware import SQLAlchemyMiddleware

# add others...

middlewares = [Middleware(SQLAlchemyMiddleware)]
