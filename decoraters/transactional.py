from functools import wraps
from database import sessionmanager


class Transactional:
    # def __init__(self, propagation: Propagation = Propagation.REQUIRED):
    # self.propagation = propagation

    def __call__(self, function):
        @wraps(function)
        async def decorator(*args, **kwargs):
            try:
                result = await function(*args, **kwargs)
                async with sessionmanager.session() as session:
                    print("commit visited? ", session)
                    await session.commit()
            except Exception as e:
                print("exception visited? ", e)
                async with sessionmanager.session() as session:
                    await session.rollback()
                raise e
            finally:
                async with sessionmanager.session() as session:
                    print("close visited? ", session)
                    await session.close()

            return result

        return decorator
