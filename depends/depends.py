from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db_session

session = Annotated[AsyncSession, Depends(get_db_session)]
