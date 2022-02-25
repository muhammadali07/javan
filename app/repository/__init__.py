import json
import gevent


from select import select
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from structlog.types import FilteringBoundLogger
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import query_expression, sessionmaker, subqueryload, joinedload
from fastapi.encoders import jsonable_encoder

from models import DataKeluargaBudi

from entities import KeluargaBudi


class BudiRepository:
    def __init__(self, engine: AsyncEngine, logger: FilteringBoundLogger) -> None:
        self.engine = engine
        self.logger = logger
        self.asyncSession = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_all_budi_family(self, request:DataKeluargaBudi):
        async with self.asyncSession as session:
            try:
                query_select = (
                    select(KeluargaBudi)
                )
                proxy_row = await session.execute(query_select)
                result = proxy_row.mappings().all()
                data = jsonable_encoder(result)

                status = "00"
                remark = "Success"
                return status, remark, data
            except gevent.Timeout:
                self.logger.warn("Get data to DB timeout")
                await session.invalidate()
                remark = "Failed, DB transaction was timed out..."
                message_id = "02"
                return None, message_id, remark

            except SQLAlchemyError as e:
                self.logger.error("Get data to DB error", error=str(e))
                await session.rollback()
                remark = "Failed, DB transaction was timed out..."
                message_id = "02"
                return None, message_id, remark
