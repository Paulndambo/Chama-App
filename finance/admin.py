from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(MemberRegistration)
admin.site.register(GroupRegistration)
admin.site.register(GroupRenewal)
admin.site.register(Fine)
admin.site.register(Saving)
admin.site.register(WeeklyPayment)
admin.site.register(GroupSaving)
admin.site.register(MembershipRenewal)
admin.site.register(MemberTotalSaving)
admin.site.register(ChamaExpenditure)

@admin.register(GroupTotalSaving)
class GroupTotalSavingAdmin(admin.ModelAdmin):
    list_display = ["group", "year", "amount"]
