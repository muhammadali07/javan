import imp
from pydantic import BaseModel
from typing import Optional

class DataKeluargaBudi(BaseModel):
    marga : Optional[str]
    anak_budi : Optional[str]
    jenis_kelamin : Optional[str]
    cucu_budi : Optional[str]
    