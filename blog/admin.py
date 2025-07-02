from django.contrib import admin
from .models import Post, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'approved', 'created_on')
    search_fields = ('body', 'author__username', 'post__title')
    list_filter = ('approved', 'created_on')

admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
