from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(MembershipRenewalLog)
admin.site.register(MemberRegistrationLog)
admin.site.register(GroupRegistrationLog)
admin.site.register(GroupRenewalLog)
admin.site.register(FineLog)
admin.site.register(SavingLog)
admin.site.register(WeeklyPaymentLog)
admin.site.register(GroupSavingLog)
admin.site.register(ChamaExpenditureLog)
