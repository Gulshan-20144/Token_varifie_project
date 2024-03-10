from django.contrib import admin
from subcompany.models import Users,company
# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display=['user_id','name','mobile','gmail','age']
       
@admin.register(company)
class UserAdmin(admin.ModelAdmin):
    list_display=['c_name','user','adminuser']