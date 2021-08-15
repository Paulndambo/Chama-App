from django.db import models
from django.utils import timezone
# Create your models here.
class MembershipRenewalLog(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member_id = models.CharField(max_length=200)
    renewal_amount = models.FloatField(default=0)
    renewal_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member_id
     
class MemberRegistrationLog(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member_id = models.CharField(max_length=200)
    amount_paid = models.FloatField(default=0)
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member_id

class GroupRegistrationLog(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    group_id = models.CharField(max_length=200)
    amount_paid = models.FloatField(default=0)
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return self.group_id

class GroupRenewalLog(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    group_id = models.CharField(max_length=200)
    amount_paid = models.FloatField(default=0)
    year = models.CharField(max_length=4)
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return self.group_id

class FineLog(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member_id= models.CharField(max_length=200)
    reason = models.TextField(default="late for meeting")
    amount_fined = models.FloatField(default=50)
    date_fined = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member_id

class SavingLog(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member_id = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    date_submitted = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member_id

class WeeklyPaymentLog(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member_id = models.CharField(max_length=200)
    amount = models.FloatField(default=500)
    year = models.CharField(max_length=4)
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member_id

class GroupSavingLog(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member_id = models.CharField(max_length=200)
    group_id = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    year = models.CharField(max_length=4)
    date_paid = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member_id + " Saved For "+self.group_id

class ChamaExpenditureLog(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=500)
    amount_spend = models.FloatField(default=0)
    description = models.TextField()
    date_spend = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

