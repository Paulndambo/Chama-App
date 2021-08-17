from django.urls import path
from . views import *

urlpatterns = [
    path("memberships/", MemberRegistrationList.as_view(), name="memberships"),
    path("add-membership/", MembershipRegistrationCreateView.as_view(), name="add-membership"),
    path("group-registrations/", GroupRegistrationList.as_view(), name="group-registrations"),
    path("register-group/", GroupRegistrationCreateView.as_view(), name="register-group"),
    path("group-renewals/", GroupRenewalList.as_view(), name="group-renewals"),
    path("renew-group/", GroupRenewalCreateView.as_view(), name="renew-group"),
    path("fines/", FinesList.as_view(), name="fines"),
    path("add-fine/", FineCreateView.as_view(), name="add-fine"),
    path("weekly-payments/", WeeklyPayments.as_view(), name="weekly-payments"),
    path("add-weekly-payment/", AddWeeklyPayment.as_view(), name="add-weekly-payment"),
    path("savings/", Savings.as_view(), name="savings"),
    path("add-savings/", AddSavings.as_view(), name="add-savings"),
    path("member-total-savings/", MemberTotalSavings.as_view(), name="member-total-savings"),
    path("group-total-savings/", GroupTotalSavings.as_view(), name="group-total-savings"),
    path("group-savings/", GroupSavings.as_view(), name="group-savings"),
    path("add-group-savings/", AddGroupSavings.as_view(), name="add-group-savings"),
    #path("dividends/", Dividends.as_view(), name="dividends"),
    path("membership-renewals/", MembershipRenewals.as_view(), name="membership-renewals"),
    path("membership-renew/", MembershipRenew.as_view(), name="membership-renew"),
    path("chama-expenditures/", ChamaExpenditures.as_view(), name="chama-expenditures"),
    path("new-chama-expenditure/", AddChamaExpenditure.as_view(), name="new-chama-expenditure"),

    #member portal
    path("member-savings/", views.member_savings, name="member-savings"),
    path("member-weekly-payments/", views.member_weekly_payments, name="member-weekly-paymnets"),
    path("current-member-total-savings/", views.current_member_total_savings, name="current-member-total-savings"),
]   
