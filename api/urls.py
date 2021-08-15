from django.urls import path, include
from . views import *
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()

#Data Urls
router.register("chama-members", MemberViewSet, basename="chama-members")
router.register("chama-staff", StaffViewSet, basename="chama-staff")
router.register("chama-groups", GroupViewSet, basename="chama-groups")
router.register("chama-meetings", MeetingViewSet, basename="chama-meetings")
router.register("chama-attendances", AttendanceViewSet, basename="chama-attendances")
router.register("chama-group-memberships", GroupMembershipViewSet, basename="chama-group-memberships")

#Finance Urls
router.register("member-registration-fees", MemberRegistrationViewSet, basename="member-registration-fees")
router.register("member-savings", SavingViewSet, basename="member-savings")
router.register("group-savings", GroupSavingViewSet, basename="group-savings")
router.register("weekly-payments", WeeklyPaymentViewSet, basename="weekly-payments")
router.register("membership-renewals", MembershipRenewalViewSet, basename="membership-renewals")
router.register("group-renewals", GroupRenewalViewSet, basename="group-renewals")
router.register("fines", FineViewSet, basename="fines")
router.register("member-total-savings", MemberTotalSavingViewSet, basename="member-total-savings")
router.register("group-total-savings", GroupTotalSavingViewSet, basename="group-total-savings")

#Lenders Urls
router.register("lenders", LenderViewSet, basename="lenders")

urlpatterns = [
    path("", include(router.urls)),
]
