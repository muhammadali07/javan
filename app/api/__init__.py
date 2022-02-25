import imp
import logging

from h11 import Data
import jwt

from typing import Dict, List, Optional
from fastapi import APIRouter, FastAPI,status
from fastapi.responses import JSONResponse

from models import DataKeluargaBudi

from application import BudiApplication

class BudiAPI(FastAPI):
    def __init__(self, app: BudiApplication, debug: bool = False, title: str = "FastAPI", description: str = "", version: str = "0.1.0", openapi_url: str = "/budi/api/v1/openapi.json", docs_url="/budi/docs", servers: List[Dict[str, str]] = None) -> None:
        super().__init__(debug=debug, title=title, description=description, version=version, openapi_url=openapi_url, docs_url=docs_url, servers=servers)
        self.app: BudiApplication = app
        budi = APIRouter(prefix="/budi/api/v1/rekening")

        @budi.get("/get-all-keluarga-budi",
            summary="Get All Keluarga Budi",
            status_code = status.HTTP_200_OK,
            tags = ['Keluarga Budi']
        )
        async def get_all_budi_family(request:DataKeluargaBudi):
            result = await self.app.get_all_budi_family(request)
            logging.debug(f'get result: {result}')
            if result["status"] == "00":
                return JSONResponse(result, status_code=status.HTTP_200_OK)
            else:
                return JSONResponse(result, status_code=status.HTTP_400_BAD_REQUEST)








        self.include_router(budi)

