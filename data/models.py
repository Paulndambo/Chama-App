from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
GENDER_CHOICES = [
    ("Female","Female"),
    ("Male","Male"),
    ("Binary", "Binary"),
]

STAFF_CHOICES = (
    ("Chairperson", "Chairperson"),
    ("Treasurer", "Treasurer"),
    ("Secretary", "Secretary"),
)

MEETING_CHOICES = (
    ("Weekly Meeting", "Weekly Meeting"),
    ("Monthly Meeting", "Monthly Meeting"),
    ("Annual Meeting", "Annual Meeting"),
    ("Board Meeting", "Board Meeting"),
    ("Emergency Meeting", "Emergency Meeting"),
)
YEAR_CHOICES = (
    ("2021", "2021"),
    ("2022", "2022"),
    ("2023", "2023"),
    ("2024", "2024"),
    ("2025", "2025"),
)
MONTH_CHOICES = (
    ("January", "January"),
    ("Febuary", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)
WEEK_CHOICES = (
    ("Week 1", "Week 1"),
    ("Week 2", "Week 2"),
    ("Week 3", "Week 3"),
    ("Week 4", "Week 4"),
    ("Week 5", "Week 5"),
    ("Week 6", "Week 6"),
    ("Week 7", "Week 7"),
    ("Week 8", "Week 8"),
    ("Week 9", "Week 9"),
    ("Week 10", "Week 10"),
)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=200, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, default="2021")
    postal_code = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def address(self):
        return self.postal_code + " , " +self.town +" - "+self.country

    def get_absolute_url(self):
        return reverse("members")

class Staff(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, choices=STAFF_CHOICES)
    date_appointed = models.DateTimeField(default=timezone.now)
    retirement_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.member.name

    def get_absolute_url(self):
        return reverse("chama-staff")

class Group(models.Model):
    group_id = models.CharField(max_length=20, unique=True, primary_key=True)
    title = models.CharField(max_length=500, unique=True)
    date_formed = models.DateField(default=timezone.now)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, default="2021")
    number_of_members = models.IntegerField(default=0)
    chairperson = models.OneToOneField(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("groups")

class Meeting(models.Model):
    meeting_code = models.CharField(max_length=30, unique=True, primary_key=True)
    meeting_title = models.CharField(max_length=200, choices=MEETING_CHOICES, unique_for_date="meeting_date")
    meeting_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.meeting_title

    class Meta:
        verbose_name_plural = ("Chama Meetings")

    def get_absolute_url(self):
        return reverse("meetings")

class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.member)

    class Meta:
        verbose_name_plural = ("Chama Attendance")

    def get_absolute_url(self):
        return reverse("attendance")

class GroupMembership(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.member) + " Joined "+str(self.group)

    def get_absolute_url(self):
        return reverse("group-membership")
