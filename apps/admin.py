from django.contrib import admin

# Register your models here.

from . models import Posts, Category , Comment, ProfileUser


admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ProfileUser)