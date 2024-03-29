from enum import StrEnum
from pydantic import BaseModel, Field, PositiveInt
from typing import Annotated
from datetime import datetime, timezone
from pydantic import (
    SerializerFunctionWrapHandler, WrapSerializer
)


def to_utc(
    utc_or_native: datetime,
    nxt: SerializerFunctionWrapHandler
) -> str:
    utc_datetime = utc_or_native.replace(
        tzinfo=timezone.utc
    )
    # 前処理をしてから元のシリアライザに戻す
    return nxt(utc_datetime)


# 第一引数が実際の型。2番目以降はメタデータ。
UTCDatetime = Annotated[
    datetime, WrapSerializer(to_utc)
]


class HistoryType(StrEnum):
    INCOME = "INCOME"
    OUTCOME = "OUTCOME"


class History(BaseModel):
    history_id: int
    name: str
    amount: PositiveInt
    type: HistoryType
    history_at: UTCDatetime


class Wallet(BaseModel):
    wallet_id: int = Field(..., ge=1)
    name: str = Field(
        ...,
        pattern="^[a-zA-z]+$",
        description="Wallet name",
    )
    histories: list[History]


class CreateWalletRequest(BaseModel):
    name: str
