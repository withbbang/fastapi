from functools import wraps
from database.connection import session


class Transactional:
    # def __init__(self, propagation: Propagation = Propagation.REQUIRED):
    # self.propagation = propagation

    def __call__(self, function):
        @wraps(function)
        async def decorator(*args, **kwargs):
            try:
                result = await function(*args, **kwargs)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.remove()
            return result

        return decorator
