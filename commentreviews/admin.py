from django.contrib import admin
from .models import Comment
from .actions import disapprove_comments, approve_comments


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'approved', 'date_comment', 'comment']
    actions = [disapprove_comments, approve_comments]
    # opção de pesquisar campos
    search_fields = ['user.username']


admin.site.register(Comment, CommentAdmin)  # Register your models here.


