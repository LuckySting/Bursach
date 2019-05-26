from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    pass


@admin.register(Brunch)
class BrunchAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
