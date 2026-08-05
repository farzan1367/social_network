from django.contrib import admin

from posts.models import Post,PostFile

class PostFileInLineAdmin(admin.StackedInline):
    model = PostFile
    fields = ('file',)
    extra = 0
    can_delete = False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','user','is_active','created_time')
    inlines = [PostFileInLineAdmin]

    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_add_permission(self, request, obj=None):
    #     return False


# @admin.register(PostFile)
# class PostFileAdmin(admin.ModelAdmin):
#     pass
