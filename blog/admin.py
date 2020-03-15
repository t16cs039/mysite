from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Status

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Status)

# Register your models here.
