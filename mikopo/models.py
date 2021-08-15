from django.db import models
from data.models import Group, Member, Staff
from django.utils import timezone
# Create your models here.
APPROVE_CHOICES = (
    ("Approve", "Approve"),
    ("Decline", "Decline"),
    ("Pending Review", "Pending Review"),
)
LOAN_DISBURSE = (
    ("Mpesa", "Mpesa"),
    ("Bank", "Bank"),
    ("Cash", "Cash"),
)
class LoanType(models.Model):
    title = models.CharField(max_length=200, unique=True, primary_key=True)
    period = models.FloatField(default=0)
    interest_rate = models.FloatField(default=0)

    def __str__(self):
        return self.title

class MemberLoanApplication(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE, default="Normal Loan")
	amount_applying = models.FloatField(default=0)
	approve_or_decline = models.CharField(max_length=50, choices=APPROVE_CHOICES, default="Pending Review")
	date_applied = models.DateField(default=timezone.now)

	def __str__(self):
		return str(self.member)

	def get_loan_status(self):
		if approve_or_decline == "Approve":
			return "Approved"
		elif approve_or_decline == "Decline":
			return "Declined"
		else:
			return "Pending Review"

class GroupLoanApplication(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_loans")
	loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE)
	amount_applying = models.FloatField(default=0)
	approve_or_decline = models.CharField(max_length=50, choices=APPROVE_CHOICES)
	date_applied = models.DateField(default=timezone.now)

	def __str__(self):
		return str(self.group)

	def get_loan_status(self):
		if approve_or_decline == "Approve":
			return "Approved"
		elif approve_or_decline == "Decline":
			return "Declined"
		else:
			return "Pending Review"

class PersonalLoan(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="member_loans")
    loan_type = models.ForeignKey(LoanType, on_delete=models.PROTECT)
    amount_applied = models.FloatField(default=0)
    amount_awarded = models.FloatField(default=0)
    disbursed_by = models.CharField(max_length=200, choices=LOAN_DISBURSE, default="Cash")
    date_awarded = models.DateField(default=timezone.now)
    repay_by = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member.name

class GroupLoan(models.Model):
	id = models.AutoField(unique=True, primary_key=True)
	group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="group_awarded_loans")
	amount_applied = models.FloatField(default=0)
	amount_awarded = models.FloatField(default=0)
	loan_type = models.ForeignKey(LoanType, on_delete=models.PROTECT)
	disbursed_by = models.CharField(max_length=200, choices=LOAN_DISBURSE, default="Cash")
	date_awarded = models.DateField(default=timezone.now)
	repay_by = models.DateField(default=timezone.now)

	def __str__(self):
		return self.group.title

class PayPersonalLoan(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	loan = models.ForeignKey(PersonalLoan, on_delete=models.CASCADE)
	amount = models.FloatField(default=0)
	date_paid = models.DateField(default=timezone.now)


class PayGroupLoan(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	loan = models.ForeignKey(GroupLoan, on_delete=models.CASCADE)
	amount = models.FloatField(default=0)
	date_paid = models.DateField(default=timezone.now)
