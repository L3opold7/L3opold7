from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified_at', )
    list_filter = ('modified_at', )
    search_fields = ('title', 'content', )
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Post, PostAdmin)
