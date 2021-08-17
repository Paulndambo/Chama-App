from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . models import *
from django.urls import reverse_lazy
# Create your views here.
def member_loans(request):
	member_loans = PersonalLoan.objects.filter(member=request.user.member.id_number)
	print(member_loans)
	return render(request, "member-loans.html", {"member_loans": member_loans})

def member_stats(request):
	member_loans_count = PersonalLoan.objects.filter(member=request.user.member.id_number).count()
	
	context = {
		"member_loans_count": member_loans_count
	}
	return render(request, "member-home", context)

def member_loan_applications(request):
	member_loan_applications = MemberLoanApplication.objects.filter(member=request.user.member.id_number)
	print(member_loan_applications)
	return render(request, "member-loans-history.html", {"member_loan_applications": member_loan_applications})

def loan_analytics(request):
	loan_values = []
	personal_loans = LoanFinancial.objects.values('personal_loans').get(year=2021)
	for item in personal_loans.values():
		personal_loans_value = item

	personal_loans_repayments = LoanFinancial.objects.values('personal_loans_repayments').get(year=2021)
	for item in personal_loans_repayments.values():
		personal_loans_payments = item

	personal_loans_profits = LoanFinancial.objects.values('personal_loans_profit').get(year=2021)
	for item in personal_loans_profits.values():
		personal_loans_profit = item
		print(personal_loans_profit)

	group_loans = LoanFinancial.objects.values('group_loans').get(year=2021)
	for item in group_loans.values():
		group_loans_value = item
		print(group_loans_value)

	group_loans_repayments = LoanFinancial.objects.values('group_loans_repayments').get(year=2021)
	for item in group_loans_repayments.values():
		group_loans_payments = item
		print(group_loans_payments)

	group_loans_profits = LoanFinancial.objects.values('group_loans_profit').get(year=2021)
	for item in group_loans_profits.values():
		group_loans_profit = item
		print(group_loans_profit)
		
		
	loan_values.append(personal_loans_value)
	loan_values.append(personal_loans_payments)
	loan_values.append(personal_loans_profit)
	loan_values.append(group_loans_value)
	loan_values.append(group_loans_payments)
	loan_values.append(group_loans_profit)
	print(loan_values)
	return render(request, "mikopo/loan-analytics.html", {"loan_values": loan_values})

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
	template_name = "mikopo/personal-loan-approve.html"

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

class DeletePersonalLoanApplicaion(DeleteView):
	model = MemberLoanApplication
	template_name = "mikopo/delete-personal-loan-application.html"
	success_url = reverse_lazy("personal-loans-applications")


class PersonalLoanDetails(DetailView):
	model = PersonalLoan
	template_name = "mikopo/personal-loan-details.html"

class GroupLoanDetails(DetailView):
	model = GroupLoan
	template_name = "mikopo/group-loan-details.html"