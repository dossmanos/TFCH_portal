from typing import List

from fastapi import APIRouter, Depends

from base import adapters
from base.models import Composition
from base.schemas import FastComposition, FastCompositions, CompostitionCreate

router = APIRouter(prefix="/api/compositions", tags=["compositions"])


@router.get("/", response_model=FastCompositions)
async def get_compositions(
    compositions: List[Composition] = Depends(adapters.retrieve_compositions),
) -> FastCompositions:
    return FastCompositions.from_qs(compositions)


@router.get("/{composition_id}", response_model=FastComposition)
async def get_composition(
    composition: Composition = Depends(adapters.retrieve_composition),
) -> FastComposition:
    return FastComposition.from_orm(composition)


@router.post("/")
def create_composition(set_polish_name: str, set_english_name: str) -> dict:
    Composition.objects.create(
        polish_name=set_polish_name, english_name=set_english_name
    )
    return {"message": "Composition added to database"}


@router.put("/{composition_id}")
def update_composition(
    composition_id: int, new_polish_name: str, new_english_name: str
) -> dict:
    Composition.objects.filter(id=composition_id).update(
        polish_name=new_polish_name, english_name=new_english_name
    )
    return {"Server info": f"Composition updated succesfully"}


@router.delete("/{composition_id}")
def delete_composition(composition_id: int) -> dict:
    composition_to_delete = Composition.objects.filter(id=composition_id)
    if composition_to_delete is not None:
        composition_to_delete.delete()
        return {"Server info": f"Composition no.{composition_id} succesfully deleted"}
    return {"Server info": f"Composition not deleted"}
