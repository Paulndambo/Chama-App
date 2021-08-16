from django.urls import path
from . import views
from . views import *
urlpatterns = [
    path("", views.index, name="index"),
    path("chama-staff/", StaffListView.as_view(), name="chama-staff"),
    path("home/", views.home, name="home"),
    path("members/", MembersListView.as_view(), name="members"),
    path("add-member/", MembersCreateView.as_view(), name="add-member"),
    path("member-details/<int:pk>/", MemberDetails.as_view(), name="member-details"),
    path("staff/", StaffListView.as_view(), name="staff"),
    path("add-staff/", StaffCreateView.as_view(), name="add-staff"),
    path("attendance/", AttendanceListView.as_view(), name="attendance"),
    path("add-attendance/", AttendanceCreateView.as_view(), name="add-attendance"),
    path("meetings/", MeetingListView.as_view(), name="meetings"),
    path("add-meeting/", MeetingCreateView.as_view(), name="add-meeting"),
    path("groups/", GroupsList.as_view(), name="groups"),
    path("add-group/", GroupCreateView.as_view(), name="add-group"),
    path("group-membership/", GroupMembershipList.as_view(), name="group-membership"),
    path("add-group-member/", GroupMembershipCreateView.as_view(), name="add-group-member"),
]
