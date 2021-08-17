from django.urls import path
from . views import *
from . import views

urlpatterns = [
	path("group-loans/", GroupLoans.as_view(), name="group-loans"),
	path("group-loan-applications/", GroupLoanApplications.as_view(), name="group-loan-applications"),
	path("group-loan-payments/", GroupLoanPayments.as_view(), name="group-loan-payments"),
	path("new-group-loan/", NewGroupLoan.as_view(), name="new-group-loan"),
	path("pay-group-loan/", PayGroupLoan.as_view(), name="pay-group-loan"),
	path("apply-group-loan/", ApplyGroupLoan.as_view(), name="apply-group-loan"),
	path("approve-group-loan/<int:pk>/", ApproveGroupLoan.as_view(), name="approve-group-loan"),
	path("personal-loans/", PersonalLoans.as_view(), name="personal-loans"),
	path("personal-loans-applications/", PersonalLoanApplications.as_view(), name="personal-loans-applications"),
	path("personal-loans-payments/", PersonalLoanPayments.as_view(), name="personal-loans-payments"),
	path("new-personal-loan/", NewPersonalLoan.as_view(), name="new-personal-loan"),
	path("pay-personal-loan/", PayPersonalLoan.as_view(), name="pay-personal-loan"),
	path("apply-personal-loan/", ApplyPersonalLoan.as_view(), name="apply-personal-loan"),
	path("approve-personal-loan/<int:pk>/", ApprovePersonalLoan.as_view(), name="approve-personal-loan"),
	path("delete-personal-loan-application/<int:pk>/", DeletePersonalLoanApplicaion.as_view(), name="delete-personal-loan-application"),

	path("loan-types/", LoanTypeList.as_view(), name="loan-types"),
	path("new-loan-type/", NewLoanType.as_view(), name="new-loan-type"),

	path("group-loan-details/<int:pk>/", GroupLoanDetails.as_view(), name="group-loan-details"),
	path("personal-loan-details/<int:pk>/", PersonalLoanDetails.as_view(), name="personal-loan-details"),

	#Analytics
	path("loan-analytics/", views.loan_analytics, name="loan-analytics"),

	#Member Portal
	path("member-loans/", views.member_loans, name="member-loans"),
	path("member-loan-applications/", views.member_loan_applications, name="member-loan-applications"),

]	