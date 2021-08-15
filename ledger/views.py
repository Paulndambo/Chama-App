from django.shortcuts import render
from django.views.generic import ListView
from . models import *
# Create your views here.
class MemberRegistrationLog(ListView):
	model = MemberRegistrationLog
	template_name = "ledger/member-registrations-fees.html"

class MembershipRenewalLog(ListView):
	model = MembershipRenewalLog
	template_name = "ledger/member-renewals.html"

class GroupRegistrationLog(ListView):
	model = GroupRegistrationLog
	template_name = "ledger/group-registration-fees.html"

class GroupRenewalLog(ListView):
	model = GroupRenewalLog
	template_name = "ledger/group-renewals.html"

class FineLog(ListView):
	model = FineLog
	template_name = "ledegr/fines.html"

class SavingLog(ListView):
	model = SavingLog
	template_name = "ledger/savings.html"

class WeeklyPaymentLog(ListView):
	model = WeeklyPaymentLog
	template_name = "ledger/weekly-payments.html"

class GroupSavingLog(ListView):
	model = GroupSavingLog
	template_name = "ledger/group-savings.html"

class ChamaExpenditureLog(ListView):
	model = ChamaExpenditureLog
	template_name = "ledger/expeditures.html"