from django.contrib import admin
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "rate", "category", "author", "createad_at", "updated_at"]
    search_fields = ["title", "content", "category_name"]
    list_filter = ["category", "tag"]
    list_editable = ["author", "age"]
    list_display_links = ["title", "content"]
    

    admin.site.register(Tag)
    admin.site.registe(Category)
                

