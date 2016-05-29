
from django.contrib import admin

from .models import Post


admin.site.site_header = "Info Blog Manager"

admin.site.register(Post)
