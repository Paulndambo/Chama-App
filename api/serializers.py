from rest_framework import serializers
from data.models import *
from finance.models import *
from lenders.models import *
from django.contrib.auth.models import User

#Loan Serializers

#Lenders serializers
class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = "__all__"

#Finance serializers
class MemberRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRegistration
        fields = "__all__"

class GroupRenewalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupRenewal
        fields = "__all__"

class MembershipRenewalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipRenewal
        fields = "__all__"

class GroupRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupRegistration
        fields = "__all__"

class WeeklyPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyPayment
        fields = "__all__"

class GroupSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSaving
        fields = "__all__"

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = "__all__"

class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = "__all__"


class GroupTotalSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupTotalSaving
        fields = "__all__"

class MemberTotalSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberTotalSaving
        fields = "__all__"

# Register Serializer
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ["member", "position", "date_appointed", "retirement_date"]

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

class GroupMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembership
        fields = "__all__"

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"
