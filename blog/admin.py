from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_diplay = (
        "title",
        "author",
        "body",
    )


admin.site.register(Post, PostAdmin)
