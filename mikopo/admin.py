from django.contrib import admin
from  .models import *
# Register your models here.
admin.site.register(GroupLoanAnalytics)
admin.site.register(PersonalLoanAnalytics)
admin.site.register(PayGroupLoan)
admin.site.register(PayPersonalLoan)
admin.site.register(GroupLoan)
admin.site.register(PersonalLoan)

admin.site.register(LoanFinancial)