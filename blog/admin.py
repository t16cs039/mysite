from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Status, Article

# Register your models here.
admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Status)
admin.site.register(Article)
