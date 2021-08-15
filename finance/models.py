from django.db import models
from data.models import Member, Group, Staff
from django.utils import timezone
from django.urls import reverse
# Create your models here.
YEAR_CHOICES = (
    ("2021", "2021"),
    ("2022", "2022"),
    ("2023", "2023"),
    ("2024", "2024"),
    ("2025", "2025"),
)

class MembershipRenewal(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    renewal_amount = models.FloatField(default=0)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, default="2021")
    date_renewed = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member.name

    def get_absolute_url(self):
        return reverse("membership-renewals")

class MemberRegistration(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    amount_paid = models.FloatField(default=1500, editable=False)
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member.name

    def get_absolute_url(self):
        return reverse("memberships")

class GroupRegistration(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    amount_paid = models.FloatField(default=2500, editable=False)
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return self.group.title

    def get_absolute_url(self):
        return reverse("group-registrations")

class GroupRenewal(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    amount_paid = models.FloatField(default=0)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, default="2021")
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return self.group.title

    def get_absolute_url(self):
        return reverse("group-renewals")

class Fine(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    reason = models.TextField(default="late for meeting")
    amount_fined = models.FloatField(default=50)
    date_fined = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member.name

    def get_absolute_url(self):
        return reverse("fines")

class Saving(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, default="2021")
    date_submitted = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member.name

    def get_absolute_url(self):
        return reverse("savings")

class WeeklyPayment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.FloatField(default=500)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, default="2021")
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member.name

    def get_absolute_url(self):
        return reverse("weekly-payments")

class GroupSaving(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, default="2021")
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member.name

    def get_absolute_url(self):
        return reverse("group-savings")

class GroupTotalSaving(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES)
    amount = models.FloatField(default=0)

    def __str__(self):
        return self.group.title

    def get_absolute_url(self):
        return reverse("group-total-savings")

class MemberTotalSaving(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES)
    amount = models.FloatField(default=0)

    def __str__(self):
        return self.member.name

    def get_absolute_url(self):
        return reverse("member-total-savings")

class ChamaIncome(models.Model):
    pass

class ChamaExpenditure(models.Model):
    transaction_number = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=500)
    amount_spend = models.FloatField(default=0)
    description = models.TextField()
    date_spend = models.DateField(default=timezone.now)
    approved_by = models.ManyToManyField(Staff)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("chama-expenditures")
