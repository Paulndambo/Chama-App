from django.urls import path
from . views import *

urlpatterns = [
	path("savings-ledger/", SavingLog.as_view(), name="savings-ledger"),
	path("group-savings-ledger/", GroupSavingLog.as_view(), name="group-savings-ledger"),
	path("memberships-ledger/", MemberRegistrationLog.as_view(), name="memberships-ledger"),
	path("memberships-renewals-ledger/", MembershipRenewalLog.as_view(), name="memberships-renewals-ledger"),
	path("group-registrations-ledger/", GroupRegistrationLog.as_view(), name="group-registrations-ledger"),
	path("group-renewals-ledger/", GroupRenewalLog.as_view(), name="group-renewals-ledger"),
	path("weekly-payments-ledger/", WeeklyPaymentLog.as_view(), name="weekly-payments-ledger"),
	path("chama-expenditures-ledger/", ChamaExpenditureLog.as_view(), name="chama-expenditures-ledger"),
	path("chama-fines-ledger/", FineLog.as_view(), name="chama-fines-ledger"),
]