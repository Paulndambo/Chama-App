from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . models import *
# Create your views here.
class GroupLoanApplications(ListView):
	model = GroupLoanApplication
	template_name = "mikopo/group-loan-applications.html"

class ApplyGroupLoan(CreateView):
	model = GroupLoanApplication
	fields = "__all__"
	template_name = "mikopo/apply-group-loan.html"

class ApproveGroupLoan(UpdateView):
	model = GroupLoanApplication
	fields = ["approve_or_decline"]
	template_name = "mikopo/group-loan-approve.html"

class GroupLoans(ListView):
	model = GroupLoan
	template_name = "mikopo/group-loans.html"

class NewGroupLoan(CreateView):
	model = GroupLoan
	fields = "__all__"
	template_name = "mikopo/new-group-loan.html"

class GroupLoanPayments(ListView):
	model = PayGroupLoan
	template_name = "mikopo/group-loan-payments.html"

class PayGroupLoan(CreateView):
	model = PayGroupLoan
	fields = "__all__"
	template_name = "mikopo/pay-group-loan.html"

class LoanTypeList(ListView):
	model = LoanType
	template_name = "mikopo/loan-types.html"

class NewLoanType(CreateView):
	model = LoanType
	fields = "__all__"
	template_name = "mikopo/new-loan-type.html"

class PersonalLoanApplications(ListView):
	model = MemberLoanApplication
	template_name = "mikopo/personal-loans-applications.html"

class ApplyPersonalLoan(CreateView):
	model = MemberLoanApplication
	fields = "__all__"
	template_name = "mikopo/apply-personal-loan.html"

class ApprovePersonalLoan(UpdateView):
	model = MemberLoanApplication
	fields = ["approve_or_decline"]
	template_name = "personal-loan-approve.html"

class PersonalLoans(ListView):
	model = PersonalLoan
	template_name = "mikopo/personal-loans.html"

class NewPersonalLoan(CreateView):
	model = PersonalLoan
	fields = "__all__"
	template_name = "mikopo/new-personal-loan.html"

class PersonalLoanPayments(ListView):
	model = PayPersonalLoan
	template_name = "mikopo/personal-loan-payments.html"

class PayPersonalLoan(CreateView):
	model = PayPersonalLoan
	fields = "__all__"
	template_name = "mikopo/pay-personal-loan.html"