from typing import List

from fastapi import APIRouter, Depends

from base import adapters
from base.models import Program
from base.schemas import FastProgram, FastPrograms

router = APIRouter(prefix="/program", tags=["programs"])

@router.get("/", response_model=None)#FastPrograms)
def get_programs(programs: List[Program] = Depends(adapters.retrieve_programs),) -> FastPrograms:
    return FastPrograms.from_qs(programs)

@router.get("/{program_id}", response_model=None)#FastProgram)
def get_Program(program: Program = Depends(adapters.retrieve_program),) -> FastProgram:
    return FastProgram.from_orm(program)