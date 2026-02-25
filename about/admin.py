from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(about)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

# Register your models here.
