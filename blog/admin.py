from django.contrib import admin
from .models import Post , Category, Comment


admin.site.registrer(Post)
admin.site.registrer(Category)
admin.site.registrer(Comment)