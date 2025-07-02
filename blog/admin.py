from django.contrib import admin
from .models import Post, PostComment

class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('sno', 'user', 'post', 'created_at', 'parent_comment')
    search_fields = ('comment', 'user__username', 'post__title')
    list_filter = ('created_at',)

admin.site.register(Post)
admin.site.register(PostComment, PostCommentAdmin)
