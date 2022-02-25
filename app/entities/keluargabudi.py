from .db import Base

from sqlalchemy import (
    Column,
    String,
    BigInteger,
    DateTime,
    Sequence,
    Numeric,
    Integer
)

from sqlalchemy.sql import func

class KeluargaBudi(Base):
    __tablename__ = "keluargabudi"

    db_id = Column(String(36), primary_key=True, unique=True, index=True)
    marga = Column(String(200))
    anak_budi = Column(String(200))
    jenis_kelamin = Column(String(30))
    cucu_budi = Column(String(200))
