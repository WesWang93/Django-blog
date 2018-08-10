from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

class PostInline(admin.TabularInline):
    model = Post

class CategoryInline(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)