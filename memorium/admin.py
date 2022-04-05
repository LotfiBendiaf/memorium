from django.contrib import admin

from .models import *

# Register your models here.
admin.site.site_header = "Memorium"
admin.site.site_title = "Memorium"
admin.site.index_title = "Memorium"

admin.site.register(Memory)
admin.site.register(Category)
