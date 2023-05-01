from typing import List

from fastapi import APIRouter, Depends

from base import adapters
from base.models import Pianist
from base.schemas import FastPianist, FastPianists

router = APIRouter(prefix="/pianist", tags=["pianists"])

@router.get("/", response_model=None)#FastPianists)
def get_pianists(pianists: List[Pianist] = Depends(adapters.retrieve_pianists),) -> FastPianists:
    return FastPianists.from_qs(pianists)

@router.get("/{pianist_id}", response_model=None)#FastPianist)
def get_Pianist(pianist: Pianist = Depends(adapters.retrieve_pianist),) -> FastPianist:
    return FastPianist.from_orm(pianist)