from django.contrib import admin

# Register your models here.
from .models import Pianist, Composition, Program, Concert

admin.site.register(Pianist)
admin.site.register(Program)
admin.site.register(Composition)
admin.site.register(Concert)