from typing import Type, TypeVar

from django.db import models
from fastapi import HTTPException, Path

from base.models import Composition,Concert,Pianist,Program

ModelT = TypeVar("ModelT", bound=models.Model)

async def retrieve_object(model_class: Type[ModelT], id: int) -> ModelT:
    instance = await model_class.objects.filter(pk=id).afirst()
    if not instance:
        raise HTTPException(status_code=404, detail="Object not found.")
    return instance


async def retrieve_composition(composition_id: int = Path(..., description="get composition from db")):
    return await retrieve_object(Composition, composition_id)

async def retrieve_concert(concert_id: int = Path(..., description="get concert from db")):
    return await retrieve_object(Concert, concert_id)

async def retrieve_pianist(pianist_id: int = Path(..., description="get pianist from db")):
    return await retrieve_object(Pianist, pianist_id)

async def retrieve_program(program_id: int = Path(..., description="get program from db")):
    return await retrieve_object(Program, program_id)


async def retrieve_compositions():
    return [composition async for composition in Composition.objects.all()]

async def retrieve_concerts():
    return [concert async for concert in Concert.objects.all()]

async def retrieve_pianists():
    return [pianist async for pianist in Pianist.objects.all()]

async def retrieve_programs():
    return [program async for program in Program.objects.all()]