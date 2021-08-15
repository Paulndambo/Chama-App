from django.shortcuts import render
from . serializers import *
from data.models import *
from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import mixins
from django.contrib.auth import login
from rest_framework import permissions
# Create your views here

#Lenders Views
class LenderViewSet(viewsets.ModelViewSet):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer


#Finance
class MemberTotalSavingViewSet(viewsets.ModelViewSet):
    queryset = MemberTotalSaving.objects.all()
    serializer_class = MemberTotalSavingSerializer

class GroupTotalSavingViewSet(viewsets.ModelViewSet):
    queryset = GroupTotalSaving.objects.all()
    serializer_class = GroupTotalSavingSerializer


class MemberRegistrationViewSet(viewsets.ModelViewSet):
    queryset = MemberRegistration.objects.all()
    serializer_class = MemberRegistrationSerializer

class GroupRenewalViewSet(viewsets.ModelViewSet):
    queryset = GroupRenewal.objects.all()
    serializer_class = GroupRenewalSerializer

class GroupSavingViewSet(viewsets.ModelViewSet):
    queryset = GroupSaving.objects.all()
    serializer_class = GroupSavingSerializer

class FineViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer

class MembershipRenewalViewSet(viewsets.ModelViewSet):
    queryset = MembershipRenewal.objects.all()
    serializer_class = MembershipRenewalSerializer

class SavingViewSet(viewsets.ModelViewSet):
    queryset = Saving.objects.all()
    serializer_class = SavingSerializer

class WeeklyPaymentViewSet(viewsets.ModelViewSet):
    queryset = WeeklyPayment.objects.all()
    serializer_class = WeeklyPaymentSerializer


#Authentication
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupMembershipViewSet(viewsets.ModelViewSet):
    queryset = GroupMembership.objects.all()
    serializer_class = GroupMembershipSerializer
