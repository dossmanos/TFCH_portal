from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Composition(models.Model):
    polish_name: str = models.TextField(max_length=100, null=True)
    english_name: str = models.TextField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.polish_name


class Program(models.Model):
    program_pianist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, unique=True)
    compositions = models.ManyToManyField(
        Composition, related_name="compositions", blank=True
    )

    class Meta:
        ordering = ["program_pianist"]

    def __str__(self) -> str:
        return self.name


class Pianist(models.Model):
    pianist = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    programs = models.ManyToManyField(Program, related_name="programs", blank=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    def __str__(self) -> str:
        return self.pianist.get_full_name()


class Concert(models.Model):
    concert_pianist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    concert_program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    concert_date = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ["concert_date"]

    def __str__(self) -> str:
        return f"Concert {self.concert_date.astimezone()}"
