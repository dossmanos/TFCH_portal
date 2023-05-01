from typing import List

from fastapi import APIRouter, Depends

from base import adapters
from base.models import Composition
from base.schemas import FastComposition, FastCompositions

router = APIRouter(prefix="/composition", tags=["compositions"])

@router.get("/", response_model=None)#FastCompositions)
def get_compositions(compositions: List[Composition] = Depends(adapters.retrieve_compositions),) -> FastCompositions:
    return FastCompositions.from_qs(compositions)

@router.get("/{composition_id}", response_model=None)#FastComposition)
def get_choice(composition: Composition= Depends(adapters.retrieve_composition)) -> FastComposition:
    return FastComposition.from_orm(composition)