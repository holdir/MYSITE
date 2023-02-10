from django.contrib import admin
from main.models import CustomUser
from main.models import Gender
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Gender)