from typing import Any, Dict, Union
from structlog.types import FilteringBoundLogger

from repository import BudiRepository

from models import DataKeluargaBudi

class BudiApplication:
    def __init__(self, repo: BudiRepository, logger: FilteringBoundLogger) -> None:
        self.repo: BudiRepository = repo
        self.logger: FilteringBoundLogger = logger

    async def get_all_budi_family(self, request:DataKeluargaBudi) -> Dict[Any,str]:
        result, msgid, remark = await self.repo.get_all_budi_family(request)
        if result is None:
            return {"status": msgid, "remark": remark, "data": None}
        else:
            result = {"rekeningTabungan": result.to_dict()}
            return {"status": "00", "remark": remark, "data": result}
