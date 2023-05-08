"""This file contains all fast API schemas for base application"""

from datetime import datetime
from typing import List
from django.db import models
from pydantic import BaseModel as _BaseModel
from django.contrib.auth import get_user_model
from base.models import Program, Composition


class BaseModel(_BaseModel):
    """A baseModel class inheriting from pydantic BaseModel"""

    @classmethod
    def from_orms(cls, instances: List[models.Model]):
        return [cls.from_orm(inst) for inst in instances]


class CompostitionCreate(_BaseModel):
    """A create composition class inheriting from pydantic BaseModel"""

    polish_name: str
    english_name: str


class FastComposition(BaseModel):
    """A composition class inheriting from BaseModel class"""

    polish_name: str
    english_name: str

    class Config:
        orm_mode = True


class FastCompositions(BaseModel):
    """A compositions class inheriting from BaseModel class"""

    items: List[FastComposition]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastComposition.from_orms(qs))


class FastConcert(BaseModel):
    """A concert class inheriting from BaseModel class"""

    concert_pianist: get_user_model()
    concert_program: Program
    concert_date: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class FastConcerts(BaseModel):
    """A concerts class inheriting from BaseModel class"""

    items: List[FastConcert]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastConcert.from_orms(qs))


class FastProgram(BaseModel):
    """A program class inheriting from BaseModel class"""

    program_pianist: get_user_model()
    name: str
    compositions: List[Composition]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class FastPrograms(BaseModel):
    """A programs class inheriting from BaseModel class"""

    items: List[FastProgram]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastProgram.from_orms(qs))


class FastPianist(BaseModel):
    """A pianist class inheriting from BaseModel class"""

    pianist: get_user_model()
    programs: Program
    # avatar is not necessary I believe

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class FastPianists(BaseModel):
    """A pianists class inheriting from BaseModel class"""

    items: List[FastPianist]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastPianist.from_orms(qs))
