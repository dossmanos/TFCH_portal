from typing import List

from fastapi import APIRouter, Depends

from base import adapters
from base.models import Concert
from base.schemas import FastConcert, FastConcerts

router = APIRouter(prefix="/concert", tags=["concerts"])

@router.get("/", response_model=None)#FastConcerts)
def get_concerts(concerts: List[Concert] = Depends(adapters.retrieve_concerts),) -> FastConcerts:
    return FastConcerts.from_qs(concerts)

@router.get("/{concert_id}", response_model=None)#FastConcert)
def get_concert(concert: Concert = Depends(adapters.retrieve_concert),) -> FastConcert:
    return FastConcert.from_orm(concert)