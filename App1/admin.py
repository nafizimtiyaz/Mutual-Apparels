from django.contrib import admin
from .models import members,board_dicription,about_us,contact


admin.site.register(members),
admin.site.register(board_dicription),
admin.site.register(about_us),
admin.site.register(contact)