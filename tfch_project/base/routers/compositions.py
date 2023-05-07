from typing import List

from fastapi import APIRouter, Depends

from base import adapters
from base.models import Composition
from base.schemas import FastComposition, FastCompositions

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
async def create_composition(set_polish_name: str, set_english_name: str) -> dict:
    try:
        Composition.objects.create(
            polish_name=set_polish_name, english_name=set_english_name
        )
        return {
            "Server info": f"New composition {set_polish_name} added succesfully to database"
        }
    except:
        return {"Server info": "Error during adding composition to database"}


@router.put("/{composition_id}")
async def update_composition(
    new_polish_name: str,
    new_english_name: str,
    composition: Composition = Depends(adapters.retrieve_composition),
) -> dict | FastComposition:
    try:
        composition_to_update = composition
        composition_to_update.polish_name = new_polish_name
        composition_to_update.english_name = new_english_name
        return FastComposition.from_orm(composition_to_update)
        # return {'Server info':f'Composition updated succesfully'}
    except:
        return {
            "Server info": f"Error during updating composition no.{composition_to_update.id}"
        }


@router.delete("/{composition_id}")
async def delete_composition(
    composition: Composition = Depends(adapters.retrieve_composition),
) -> dict:
    try:
        composition_to_delete = composition
        composition_name = composition.polish_name
        composition_to_delete.delete()
        return {"Server info": f"composition {composition_name} has been removed"}
    except:
        return {"Server info": "Error during deleting composition"}
