from datetime import datetime
from typing import List

from django.db import models
from pydantic import BaseModel as _BaseModel
from base.models import Program, Composition
from django.contrib.auth.models import User


class BaseModel(_BaseModel):
    @classmethod
    def from_orms(cls, instances: List[models.Model]):
        return [cls.from_orm(inst) for inst in instances]


class FastComposition(BaseModel):
    polish_name: str
    english_name: str

    class Config:
        orm_mode = True


class FastCompositions(BaseModel):
    items: List[FastComposition]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastComposition.from_orms(qs))


class FastConcert(BaseModel):
    concert_pianist: User
    concert_program: Program
    concert_date: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class FastConcerts(BaseModel):
    items: List[FastConcert]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastConcert.from_orms(qs))


class FastProgram(BaseModel):
    program_pianist: User
    name: str
    compositions: List[Composition]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class FastPrograms(BaseModel):
    items: List[FastProgram]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastProgram.from_orms(qs))


class FastPianist(BaseModel):
    pianist: User
    programs: Program
    # avatar is not necessary I believe

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class FastPianists(BaseModel):
    items: List[FastPianist]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastPianist.from_orms(qs))
