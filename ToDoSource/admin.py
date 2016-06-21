from django.contrib import admin
from .models import UserProfileTbl
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'emailid', 'password', 'avatar_url')

admin.site.register(UserProfileTbl, UserProfileAdmin)