from django.shortcuts import render
from . models import *
from django.views.generic import ListView, CreateView
# Create your views here.
class ChamaExpenditures(ListView):
	model = ChamaExpenditure
	template_name = "finance/expeditures.html"

class AddChamaExpenditure(CreateView):
	model = ChamaExpenditure
	fields = "__all__"
	template_name = "finance/new_expediture.html"

class MembershipRenew(CreateView):
	model = MembershipRenewal
	fields = "__all__"
	template_name = "finance/membership_renew.html"

class MembershipRenewals(ListView):
	model = MembershipRenewal
	template_name = "finance/membership_renewals.html"

class MembershipRegistrationCreateView(CreateView):
	model = MemberRegistration
	fields = "__all__"
	template_name = "finance/add_membership.html"

class MemberRegistrationList(ListView):
	model = MemberRegistration
	template_name = "finance/memberships.html"

class GroupRegistrationList(ListView):
	model = GroupRegistration
	template_name = "finance/group_registrations.html"

class GroupRegistrationCreateView(CreateView):
	model = GroupRegistration
	fields = "__all__"
	template_name = "finance/register_group.html"

class GroupRenewalList(ListView):
	model = GroupRenewal
	template_name = "finance/group_renewals.html"

class GroupRenewalCreateView(CreateView):
	model = GroupRenewal
	fields = "__all__"
	template_name = "finance/renew_group.html"

class FinesList(ListView):
	model = Fine
	template_name = "finance/fines.html"

class FineCreateView(CreateView):
	model = Fine
	fields = "__all__"
	template_name = "finance/add_fine.html"

class WeeklyPayments(ListView):
	model = WeeklyPayment
	template_name = "finance/weekly_payments.html"

class AddWeeklyPayment(CreateView):
	model = WeeklyPayment
	fields = "__all__"
	template_name = "finance/add_weekly_payment.html"

class Savings(ListView):
	model = Saving
	template_name = "finance/savings.html"

class AddSavings(CreateView):
	model = Saving
	fields = "__all__"
	template_name = "finance/add_savings.html"

class MemberTotalSavings(ListView):
	model = MemberTotalSaving
	template_name = "finance/total_savings.html"

class GroupTotalSavings(ListView):
	model = GroupTotalSaving
	template_name = "finance/group_total_savings.html"

class GroupSavings(ListView):
	model = GroupSaving
	template_name = "finance/group_savings.html"

class AddGroupSavings(CreateView):
	model = GroupSaving
	fields = "__all__"
	template_name = "finance/add_group_savings.html"

#class Dividends(ListView):
#	model = Dividends
#	template_name = "finance/dividends.html"
