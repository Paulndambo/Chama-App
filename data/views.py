from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . models import *
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, "home.html")

def home(request):
    users = User.objects.all().count()
    members = Member.objects.all().count()
    staff = Staff.objects.all().count()
    groups = Group.objects.all().count()

    context = {
        "users": users,
        "members": members,
        "staff": staff,
        "groups": groups
    }
    return render(request, "index.html", context)

class GroupsList(ListView):
    model = Group
    template_name = "data/groups.html"

class GroupCreateView(CreateView):
    model = Group
    fields = "__all__"
    template_name = "data/add_group.html"

class GroupMembershipList(ListView):
    model = GroupMembership
    template_name = "data/group_members.html"

class GroupMembershipCreateView(CreateView):
    model = GroupMembership
    fields = "__all__"
    template_name = "data/add_group_member.html"

class MembersListView(ListView):
    model = Member
    template_name = "data/members.html"

class MembersCreateView(CreateView):
    model = Member
    fields = '__all__'
    template_name = "data/add_member.html"

class MemberDetails(DetailView):
    model = Member
    template_name = "data/member-details.html"

class StaffListView(ListView):
    model = Staff
    template_name = "data/staff.html"

class StaffCreateView(CreateView):
    model = Staff
    fields = '__all__'
    template_name = "data/add_staff.html"

class MeetingListView(ListView):
    model = Meeting
    template_name = "data/meetings.html"

class MeetingCreateView(CreateView):
    model = Meeting
    fields = '__all__'
    template_name = "data/add_meeting.html"

class AttendanceListView(ListView):
    model = Attendance
    template_name = "data/attendance.html"


class AttendanceCreateView(CreateView):
    model = Attendance
    fields = '__all__'
    template_name = "data/add_attendance.html"
