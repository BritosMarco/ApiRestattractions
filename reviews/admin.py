from django.contrib import admin
from .models import ReviewsComment


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['user.username', 'score', 'date_comment']
    # opção de pesquisar campos
    search_fields = ['user.username']


admin.site.register(ReviewsComment)  # Register your models here.
