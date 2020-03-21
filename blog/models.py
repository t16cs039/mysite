from django.db import models

import datetime
from django.utils import timezone

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=140)
    thumbnail = models.ImageField(upload_to='thumbnail/', null=True)
    post_time = models.DateField(null=True)
    summary = models.TextField(blank=True)
    contents = MarkdownxField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    # 管理者画面での表示
    def __str__(self):
        return self.title

    # 管理者画面でのプレビュー表示
    def formatted_markdown(self):
        return markdownify(self.contents)