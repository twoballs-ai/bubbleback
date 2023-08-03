from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Canvas)
admin.site.register(models.Node)
admin.site.register(models.Post)
admin.site.register(models.Block)
admin.site.register(models.Edge)
# admin.site.register(models.DataEdge)
