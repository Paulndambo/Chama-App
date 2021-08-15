from django.contrib import admin
from . models import Member, Staff, Group
# Register your models here.
admin.site.register(Staff)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "phone_number", "email", "country"]

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["group_id", "title", "year", "chairperson"]
