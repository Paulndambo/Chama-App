from django.db import models
from data.models import Group, Member, Staff
from django.utils import timezone
from django.urls import reverse
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

INTEREST_RATE_CHOICES = [
    ("Short Loan", (
        (15, 15),
        )
    ),
    ("Emergency Loan", (
        (5, 5),
        )
    ),
    ("Normal Loan", (
        (15, 15),
        )
    ),
    ("Development Loan", (
        (10, 10),
        )
    ),
    ("Group Loan", (
        (16, 16),
        )
    ),
]

class LoanType(models.Model):
    title = models.CharField(max_length=200, unique=True, primary_key=True)
    period = models.FloatField(default=0)
    interest_rate = models.FloatField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse("loan-types")

class MemberLoanApplication(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE, default="Normal Loan")
	amount_applying = models.FloatField(default=0)
	approve_or_decline = models.CharField(max_length=50, choices=APPROVE_CHOICES, default="Pending Review")
	date_applied = models.DateField(default=timezone.now)

	def __str__(self):
		return str(self.member)

	def get_absolute_url(self):
		return reverse("personal-loans-applications")

	def get_loan_status(self):
		if self.approve_or_decline == "Approve":
			return "Approved"
		elif self.approve_or_decline == "Decline":
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

	def get_absolute_url(self):
		return reverse("group-loan-applications")

	def get_loan_status(self):
		if self.approve_or_decline == "Approve":
			return "Approved"
		elif self.approve_or_decline == "Decline":
			return "Declined"
		else:
			return "Pending Review"

class PersonalLoan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="member_loans")
    loan_type = models.ForeignKey(LoanType, on_delete=models.PROTECT)
    amount_applied = models.FloatField(default=0)
    amount_awarded = models.FloatField(default=0)
    amount_repaid = models.FloatField(default=0)
    disbursed_by = models.CharField(max_length=200, choices=LOAN_DISBURSE, default="Cash")
    date_awarded = models.DateField(default=timezone.now)
    repay_by = models.DateField(default=timezone.now)
    year = models.IntegerField(default=timezone.now().year)

    def __str__(self):
        return self.member.name

    def get_absolute_url(self):
    	return reverse("personal-loans")

    def get_amount_to_repay(self):
    	return (self.amount_awarded * (self.loan_type.interest_rate/100)) + self.amount_awarded

    def get_balance(self):
    	return ((self.amount_awarded * (self.loan_type.interest_rate/100)) + self.amount_awarded) - self.amount_repaid

class GroupLoan(models.Model):
	group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="group_awarded_loans")
	amount_applied = models.FloatField(default=0)
	amount_awarded = models.FloatField(default=0)
	loan_type = models.ForeignKey(LoanType, on_delete=models.PROTECT)
	amount_repaid = models.FloatField(default=0)
	disbursed_by = models.CharField(max_length=200, choices=LOAN_DISBURSE, default="Cash")
	date_awarded = models.DateField(default=timezone.now)
	repay_by = models.DateField(default=timezone.now)
	year = models.IntegerField(default=timezone.now().year)

	def __str__(self):
		return self.group.title

	def get_absolute_url(self):
		return reverse("group-loans")

	def get_amount_to_repay(self):
		return (self.amount_awarded * (self.loan_type.interest_rate/100)) + self.amount_awarded

	def get_balance(self):
		return ((self.amount_awarded * (self.loan_type.interest_rate/100)) + self.amount_awarded) - self.amount_repaid


class PayPersonalLoan(models.Model):
	personalloan = models.ForeignKey(PersonalLoan, on_delete=models.SET_NULL, null=True)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	amount = models.FloatField(default=0)
	date_paid = models.DateField(default=timezone.now)
	year = models.IntegerField(default=timezone.now().year)

	def __str__(self):
		return str(self.member)

	def get_absolute_url(self):
		return reverse("personal-loans-payments")


class PayGroupLoan(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	group_loan = models.ForeignKey(GroupLoan, on_delete=models.CASCADE)
	amount = models.FloatField(default=0)
	date_paid = models.DateField(default=timezone.now)
	year = models.IntegerField(default=timezone.now().year)

	def __str__(self):
		return str(self.member)

	def get_absolute_url(self):
		return reverse("group-loan-payments")

class PersonalLoanAnalytics(models.Model):
	loans_awarded = models.FloatField(default=0)
	loans_repayment = models.FloatField(default=0)

class GroupLoanAnalytics(models.Model):
	loans_awarded = models.FloatField(default=0)
	loans_repayment = models.FloatField(default=0)

class LoanFinancial(models.Model):
	personal_loans = models.FloatField(default=0)
	personal_loans_repayments = models.FloatField(default=0)
	personal_loans_profit = models.FloatField(default=0)
	group_loans = models.FloatField(default=0)
	group_loans_repayments = models.FloatField(default=0)
	group_loans_profit = models.FloatField(default=0)
	year = models.IntegerField(default=timezone.now().year)

	def __str__(self):
		return "Loan Financial Statement"