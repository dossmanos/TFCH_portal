"""This file contains all data base models"""

import datetime
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Composition(models.Model):
    """A composition model"""
    polish_name: str = models.TextField(max_length=100, null=True)
    english_name: str = models.TextField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.polish_name


class Program(models.Model):
    """A program model"""
    program_pianist = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, unique=True)
    compositions = models.ManyToManyField(
        Composition, related_name="compositions", blank=True
    )

    class Meta:
        ordering = ["program_pianist"]

    def __str__(self) -> str:
        return self.name


class Pianist(models.Model):
    """A pianist model"""
    pianist = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True)
    programs = models.ManyToManyField(Program, related_name="programs", blank=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    def __str__(self) -> str:
        return self.__str__()


class Concert(models.Model):
    """A concert model"""
    concert_pianist = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    concert_program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    concert_date = models.DateField(default=datetime.date)

    class Meta:
        ordering = ["concert_date"]

    def __str__(self) -> str:
        return f"Concert {self.concert_date.astimezone()}"
